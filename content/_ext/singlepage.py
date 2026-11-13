"""Fixes for the single-page builders (simplepdf, singlehtml) under Sphinx 9.

With every document on one page:

1. Ids collide between documents: docutils numbers the ids it generates
   (id1, id2...) from 1 in each document, and sections with the same title
   (Introduction, Conclusion...) get the same id. A link then jumps to the
   first one in the whole book, and sphinx-simplepdf's own handling of
   duplicate sections crashes on headings without a section number. These
   ids are prefixed with the document name, along with the references to them.

2. A link to a section or label in another document comes out as
   "#document-<doc>#<anchor>". Up to Sphinx 8, the builder rewrote it to
   "#<anchor>" (SingleFileHTMLBuilder.fix_refuris); Sphinx 9 no longer does, so
   weasyprint can't follow these links and drops them from the PDF. They are
   rewritten to the (possibly prefixed) anchor, in the page context, to cover
   the body and the table of contents (toctree).
"""

import re
from collections import defaultdict

from docutils import nodes
from sphinx import addnodes

SINGLE_PAGE_BUILDERS = ('simplepdf', 'singlehtml')

_GENERATED_ID = re.compile(r'id\d+')
_DOUBLE_ANCHOR = re.compile(r'href="#document-([^"#]*)#([^"]*)"')


def _elements_by_document(node, doc=None):
    """Yield (element, name of the innermost included document) for the tree.

    Walks down from the root: in the assembled single-page tree, the parent
    links of the included documents' nodes are stale, so walking up won't do.
    """
    if isinstance(node, addnodes.start_of_file):
        doc = node['docname']
    if isinstance(node, nodes.Element):
        yield node, doc
        for child in node.children:
            yield from _elements_by_document(child, doc)


def make_ids_unique(app, doctree, docname):
    if app.builder.name not in SINGLE_PAGE_BUILDERS or docname != app.config.root_doc:
        return
    elements = list(_elements_by_document(doctree))

    documents_of_id = defaultdict(set)
    for node, doc in elements:
        for node_id in node['ids']:
            documents_of_id[node_id].add(doc)

    def needs_prefix(node_id):
        return _GENERATED_ID.fullmatch(node_id) or len(documents_of_id[node_id]) > 1

    renames = {}  # (document, old id) -> new id
    for node, doc in elements:
        if doc is None:
            continue
        new_ids = []
        for node_id in node['ids']:
            if needs_prefix(node_id):
                renames[doc, node_id] = f"{doc.replace('/', '-')}-{node_id}"
                node_id = renames[doc, node_id]
            new_ids.append(node_id)
        node['ids'] = new_ids
    for node, doc in elements:
        if node.get('refid') and (doc, node['refid']) in renames:
            node['refid'] = renames[doc, node['refid']]
        if node.get('backrefs'):
            node['backrefs'] = [renames.get((doc, ref), ref) for ref in node['backrefs']]

    app.builder.singlepage_renames = renames


def fix_page_context(app, pagename, templatename, context, doctree):
    if app.builder.name not in SINGLE_PAGE_BUILDERS:
        return
    renames = getattr(app.builder, 'singlepage_renames', {})

    def fix_links(html):
        def target(match):
            doc, anchor = match[1], match[2]
            return f'href="#{renames.get((doc, anchor), anchor)}"'

        return _DOUBLE_ANCHOR.sub(target, html)

    for key in ('body', 'toc'):
        if isinstance(context.get(key), str):
            context[key] = fix_links(context[key])
    toctree = context.get('toctree')
    if callable(toctree):
        context['toctree'] = lambda **kwargs: fix_links(toctree(**kwargs))


def setup(app):
    app.connect('doctree-resolved', make_ids_unique)
    app.connect('html-page-context', fix_page_context)
    return {'parallel_read_safe': True, 'parallel_write_safe': True}
