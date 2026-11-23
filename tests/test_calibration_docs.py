import re
from pathlib import Path

CONTENT = Path(__file__).resolve().parent.parent / 'content'

TRI = 'firmware/etalonnage-triphase.rst'
TITLES = ['Ce qu’il vous faut', 'Étalonner avec le configurateur', 'Vérifier', 'Pour aller plus loin']


def read(path: str) -> str:
    """Text of a file under content/, UTF-8, line endings normalised to LF."""
    return (CONTENT / path).read_text(encoding='utf-8').replace('\r\n', '\n')


def section_order(text: str) -> list[str]:
    """Titles underlined with '-', in order."""
    lines = text.split('\n')
    return [
        lines[i - 1].strip()
        for i in range(1, len(lines))
        if lines[i - 1].strip() and re.fullmatch(r'-{3,}', lines[i].strip()) and len(lines[i].strip()) >= len(lines[i - 1].strip())
    ]


def with_includes(path: str) -> str:
    """The page text with its '.. include::' lines replaced by the included files."""
    base = (CONTENT / path).parent

    def expand(m):
        target = (base / m.group(1).strip()).resolve()
        return target.read_text(encoding='utf-8').replace('\r\n', '\n')

    return re.sub(r'^\.\. include:: (.+)$', expand, read(path), flags=re.M)


def section_body(text: str, title: str) -> str:
    """Text of the '-' section called title, up to the next '-' section."""
    lines = text.split('\n')
    start = None
    for i in range(1, len(lines)):
        if re.fullmatch(r'-{3,}', lines[i].strip()) and lines[i - 1].strip():
            if start is not None:
                return '\n'.join(lines[start:i - 1])
            if lines[i - 1].strip() == title:
                start = i + 1
    return '\n'.join(lines[start:]) if start is not None else ''


def test_tri_section_order():
    order = section_order(read(TRI))
    assert all(t in order for t in TITLES), order
    assert [order.index(t) for t in TITLES] == sorted(order.index(t) for t in TITLES)


def test_tri_mandatory_first():
    text = read(TRI)
    assert 'obligatoire' in text
    assert text.index('obligatoire') < text.index('Ce qu’il vous faut')


def test_tri_configurator_before_formula():
    text = read(TRI)
    ref = text.index(':ref:`configurateur <configurateur-triphase>`')
    formulas = [text.find(s) for s in ('× appareil / routeur', 'valeur actuelle ×') if s in text]
    assert ref < min(formulas)
    assert ref < text.index('f_{powerCal}')


def test_tri_linky_is_total():
    body = section_body(read(TRI), 'Ce qu’il vous faut')
    assert 'Linky' in body
    assert 'une seule phase' in body or 'une phase' in body


def test_shared_intro_no_contradiction():
    assert "sans nécessiter d'étalonnage" not in with_includes(TRI)
    assert 'sans nécessiter d’étalonnage' not in with_includes(TRI)
