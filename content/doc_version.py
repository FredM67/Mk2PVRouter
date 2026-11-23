"""Which version of the documentation is being built (stable, dev, legacy, other branch)."""

ROOT = '/Mk2PVRouter/'

VERSIONS = [
    ('stable', ROOT),
    ('dev', ROOT + 'branch/dev/'),
    ('legacy', ROOT + 'branch/legacy/'),
]


def describe(branch):
    """Describe the version built from `branch` (None, '' or 'HEAD' mean main)."""
    if not branch or branch == 'HEAD':
        branch = 'main'
    if branch == 'main':
        name, base = 'stable', ROOT
    elif branch in ('dev', 'legacy'):
        name, base = branch, ROOT + 'branch/' + branch + '/'
    else:
        name, base = branch, ROOT + 'branch/' + branch.replace('/', '--') + '/'
    return {
        'branch': branch,
        'name': name,
        'base': base,
        'is_stable': branch == 'main',
        'versions': list(VERSIONS),
    }
