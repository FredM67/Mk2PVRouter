"""Fixes for the single-page builders (simplepdf, singlehtml) under Sphinx 9.

With every document on one page:

1. A link to a section or label in another document comes out as
   "#document-<doc>#<anchor>". Up to Sphinx 8, the builder rewrote it to
   "#<anchor>" (SingleFileHTMLBuilder.fix_refuris); Sphinx 9 no longer does, so
   weasyprint can't follow these links and drops them from the PDF. The last
   anchor alone is the right target. Fixed in the page context, to cover the
   body and the table of contents (toctree).

2. Docutils numbers the ids it generates (id1, id2...) from 1 in each
   document, so they collide: the "back to contents" link of a heading, or its
   permalink, jumps to the first id3 of the whole book. They are prefixed with
   the document name, along with the references to them.
"""

import re

from docutils import nodes
from sphinx import addnodes

SINGLE_PAGE_BUILDERS = ('simplepdf', 'singlehtml')

_DOUBLE_ANCHOR = re.compile(r'href="#document-[^"#]*#')
_GENERATED_ID = re.compile(r'id\d+')


def _fix_links(html):
    return _DOUBLE_ANCHOR.sub('href="#', html)


def fix_page_context(app, pagename, templatename, context, doctree):
    if app.builder.name not in SINGLE_PAGE_BUILDERS:
        return
    for key in ('body', 'toc'):
        if isinstance(context.get(key), str):
            context[key] = _fix_links(context[key])
    toctree = context.get('toctree')
    if callable(toctree):
        context['toctree'] = lambda **kwargs: _fix_links(toctree(**kwargs))


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


def prefix_generated_ids(app, doctree, docname):
    if app.builder.name not in SINGLE_PAGE_BUILDERS or docname != app.config.root_doc:
        return
    elements = [(node, doc) for node, doc in _elements_by_document(doctree) if doc]
    renames = {}  # (document, old id) -> new id
    for node, doc in elements:
        new_ids = []
        for node_id in node['ids']:
            if _GENERATED_ID.fullmatch(node_id):
                renames[doc, node_id] = f"{doc.replace('/', '-')}-{node_id}"
                node_id = renames[doc, node_id]
            new_ids.append(node_id)
        node['ids'] = new_ids
    for node, doc in elements:
        if node.get('refid') and (doc, node['refid']) in renames:
            node['refid'] = renames[doc, node['refid']]
        if node.get('backrefs'):
            node['backrefs'] = [renames.get((doc, ref), ref) for ref in node['backrefs']]


def setup(app):
    app.connect('doctree-resolved', prefix_generated_ids)
    app.connect('html-page-context', fix_page_context)
    return {'parallel_read_safe': True, 'parallel_write_safe': True}
