from datetime import datetime


extensions = []
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'

project = u'Cygnus'
year = datetime.now().year
copyright = u'%d Jeff Forcier' % year

exclude_patterns = ['_build']

html_theme = 'cygnus'
html_sidebars = {
    '**': [
        'about.html',
        'navigation.html',
        'relations.html',
        'searchbox.html',
        'donate.html',
    ]
}
html_theme_options = {
    'description': "A light, configurable Sphinx theme",
    'github_user': 'bitprophet',
    'github_repo': 'cygnus',
    'fixed_sidebar': True,
}

extensions.append('releases')
releases_github_path = 'bitprophet/cygnus'
# Our pre-0.x releases are unstable / mix bugs+features
releases_unstable_prehistory = True
