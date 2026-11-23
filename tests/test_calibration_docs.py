import re
from pathlib import Path

import pytest

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


MONO = 'firmware/etalonnage-monophase.rst'


def test_mono_section_order():
    order = section_order(read(MONO))
    assert all(t in order for t in TITLES), order
    assert [order.index(t) for t in TITLES] == sorted(order.index(t) for t in TITLES)


def test_mono_top_box_has_relays():
    text = read(MONO)
    first = re.search(r'^\.\. (?:tip|note|admonition)::.*?(?=^\S)', text, flags=re.M | re.S).group(0)
    assert 'relais' in first and 'triac' in first


def test_mono_readings_and_values():
    text = read(MONO)
    for s in ('``P``', '``V``', '``diverted``', 'f_powerCalOldBoard', 'f_powerCalDivertedOldBoard',
              'f_voltageCalOldBoard', 'f_ctRating', 'f_ctRatingDiverted', 'f_powerCalPerAmp',
              'f_voltageCalNewBoard'):
        assert s in text, s


def test_mono_ct2_reading_is_safe():
    text = read(MONO)
    assert '.. danger::' in text
    assert text.index('.. danger::') < text.index('à travers CT2')
    assert 'ne commute jamais' in text


def test_mono_no_old_firmware():
    text = read(MONO)
    for s in ('cal_CT1_v_meter', 'cal_CT2_v_CT1', 'powerCal_grid', 'powerCal_diverted', 'Mk2_fasterControl_Full'):
        assert s not in text, s


def test_calibration_pages_have_only_the_four_sections():
    for page in (TRI, MONO):
        assert section_order(read(page)) == TITLES, page


def test_calibration_pages_do_not_include_a_shared_intro():
    for page in (TRI, MONO):
        assert 'etalonnage-intro' not in read(page), page


def test_tri_does_not_say_calibration_is_unneeded():
    text = read(TRI)
    assert 'sans nécessiter' not in text
    assert 'obligatoire' in text


def test_mono_is_single_phase():
    assert 'chaque phase' not in read(MONO)


def test_mono_linky_is_apparent_power():
    body = section_body(read(MONO), 'Ce qu’il vous faut')
    assert 'Linky' in body and 'VA' in body


def _etalonnage_section(path: str) -> str:
    """Text of the '-' section called « Étalonnage » of a configurator page."""
    return section_body(read(path), 'Étalonnage')


@pytest.mark.parametrize('page,label', [
    ('firmware/configurateur-triphase.rst', 'etalonnage-triphase'),
    ('firmware/configurateur-monophase.rst', 'etalonnage-monophase'),
])
def test_configurator_calibration_points_to_page(page, label):
    body = _etalonnage_section(page)
    assert body.strip(), page
    assert f':ref:`{label}`' in body, page
    assert not re.search(r'^\s*(?:#\.|\d+\.)\s', body, flags=re.M), page


OLD_FIRMWARE_NAMES = [
    'Mk2_fasterControl_Full', 'cal_CT1_v_meter', 'cal_CT2_v_CT1', 'powerCal_grid', 'powerCal_diverted',
    'OLD_PCB', 'physicalPin_dump_load', 'forcePin', 'dumpLoad_startup_sequence', 'TEMP_ENABLED', 'sensor_list',
]
ANCIEN = 'common/ancien-firmware-monophase.inc.rst'
MONO_INSTALL = 'firmware/logiciel-monophase.rst'
MONO_INC = 'firmware/firmware-monophase.inc.rst'


def test_no_old_firmware_anywhere():
    hits = []
    for p in sorted(CONTENT.rglob('*.rst')):
        rel = p.relative_to(CONTENT).as_posix()
        if rel == ANCIEN:
            continue
        text = p.read_text(encoding='utf-8')
        hits += [f'{rel}: {n}' for n in OLD_FIRMWARE_NAMES if n in text]
    assert not hits, hits


def test_mono_install_names_new_firmware():
    assert 'Mk2_1phase_RFdatalog_temp' in read(MONO_INSTALL)
    assert 'Mk2_1phase_RFdatalog_temp' in read(MONO_INC)
    text = read(MONO_INSTALL)
    assert '.. include:: ../common/ancien-firmware-monophase.inc.rst' in text
    assert ':ref:`configurateur-monophase`' in text or '<configurateur-monophase>' in text


def test_mono_steps_not_mandatory():
    text = read(MONO_INSTALL)
    assert not re.search(r'OBLIGATOIRE', text)
    step = text[text.index('**Étalonnage**'):]
    step = step[:step.index('#. **Installation finale**')]
    assert 'relais' in step
