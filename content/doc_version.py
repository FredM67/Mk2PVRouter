"""Which version of the documentation is being built (stable, dev, legacy, other branch)."""

ROOT = '/Mk2PVRouter/'

VERSIONS = [
    ('stable', ROOT),
    ('dev', ROOT + 'branch/dev/'),
    ('legacy', ROOT + 'branch/legacy/'),
]


def detect_branch(env, fallback=lambda: None):
    """The branch being built: DOC_BRANCH (CI), else GITHUB_REF (refs/heads/*), else `fallback()`.

    GITHUB_* variables cannot be overridden in a workflow, hence DOC_BRANCH.
    A pull request (refs/pull/...) or a detached HEAD gives no branch name,
    and describe() then treats it as stable.
    """
    branch = env.get('DOC_BRANCH', '')
    if branch:
        return branch
    ref = env.get('GITHUB_REF', '')
    if ref.startswith('refs/heads/'):
        return ref[len('refs/heads/'):]
    return fallback()


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
