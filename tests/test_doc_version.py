import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / 'content'))

from doc_version import describe  # noqa: E402

STABLE = '/Mk2PVRouter/'
DEV = '/Mk2PVRouter/branch/dev/'
LEGACY = '/Mk2PVRouter/branch/legacy/'


def test_main_is_stable():
    d = describe('main')
    assert (d['branch'], d['name'], d['base'], d['is_stable']) == ('main', 'stable', STABLE, True)


def test_dev():
    d = describe('dev')
    assert (d['name'], d['base'], d['is_stable']) == ('dev', DEV, False)


def test_legacy():
    d = describe('legacy')
    assert (d['name'], d['base'], d['is_stable']) == ('legacy', LEGACY, False)


def test_other_branch_slash_becomes_double_dash():
    d = describe('feat/x')
    assert (d['branch'], d['name'], d['base']) == ('feat/x', 'feat/x', '/Mk2PVRouter/branch/feat--x/')
    assert not d['is_stable']


def test_unknown_branch_is_stable():
    for branch in (None, 'HEAD', ''):
        d = describe(branch)
        assert (d['branch'], d['name'], d['base'], d['is_stable']) == ('main', 'stable', STABLE, True)


def test_versions_list():
    assert describe('feat/x')['versions'] == [('stable', STABLE), ('dev', DEV), ('legacy', LEGACY)]
