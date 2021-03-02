$PROJECT = 'xpdconf'
$ACTIVITIES = ['version_bump',
               'changelog',
               'tag',
               'push_tag',
               # 'ghrelease',
               'pypi'
]

$VERSION_BUMP_PATTERNS = [
    ('{}/__init__.py'.format($PROJECT.lower()), '__version__*=.*', "__version__ = '$VERSION'"),
    ('setup.py', 'version*=.*,', "version='$VERSION',")
    ]
$CHANGELOG_FILENAME = 'CHANGELOG.rst'
$CHANGELOG_IGNORE = ['TEMPLATE.rst']

$GITHUB_ORG = 'xpdAcq'
$GITHUB_REPO = 'xpdConf'
$TAG_REMOTE = 'git@github.com:xpdAcq/{}.git'.format($GITHUB_REPO)

$LICENSE_URL = 'https://github.com/{}/{}/blob/master/LICENSE'.format($GITHUB_ORG, $GITHUB_REPO)

from urllib.request import urlopen
rns = urlopen('https://raw.githubusercontent.com/xpdAcq/mission-control/master/tools/release_not_stub.md').read().decode('utf-8')
$GHRELEASE_PREPEND = rns.format($LICENSE_URL, $PROJECT.lower())
