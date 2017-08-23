# -*- coding: utf-8 -*-
import sys
import os
import datetime
import sphinx_bootstrap_theme

# Sphinx needs to be able to import the package to use autodoc and get the
# version number
sys.path.append(os.path.pardir)

from geometric import __version__

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx.ext.doctest',
    'sphinx.ext.viewcode',
    'sphinx.ext.extlinks',
    'numpydoc',
    'nbsphinx',
    'matplotlib.sphinxext.plot_directive',
    'sphinx_gallery.gen_gallery',
]

# Sphinx project configuration
templates_path = ['_templates']
exclude_patterns = ['_build', '.ipynb_checkpoints']
source_suffix = '.rst'
# The encoding of source files.
source_encoding = 'utf-8-sig'
master_doc = 'index'

# General information about the project
year = datetime.date.today().year
project = u'Geometric'
copyright = u'2017, Leonardo Uieda'
if len(__version__.split('+')) > 1 or __version__ == 'unknown':
    version = 'dev'
else:
    version = __version__

# Produce pages for each class and function
autosummary_generate = True
autodoc_default_flags = []

numpydoc_class_members_toctree = False

# Configure the sphinx-gallery plugin
sphinx_gallery_conf = {
    'examples_dirs': ['../gallery', '../tutorial'],
    'gallery_dirs': ['gallery', 'tutorial'],
    'filename_pattern': os.sep + '*', # Match any .py file
     # directory where function granular galleries are stored
    'backreferences_dir' : 'backreferences',
    # Modules for which unction level galleries are created.  In
    # this case sphinx_gallery and numpy in a tuple of strings.
    'doc_module': ('geometric', ),
    # The module you locally document uses a None
    'reference_url': {'geometric': None},
}

# Configure the inline plots from matplotlib plot_directive
plot_formats = [("png", 90)]
plot_html_show_formats = False
plot_html_show_source_link = False

# These enable substitutions using |variable| in the rst files
rst_epilog = """
.. |year| replace:: {year}
""".format(year=year)

html_last_updated_fmt = '%b %d, %Y'
html_title = project
html_short_title = 'geometric'
# html_logo = '_static/fatiando-navbar-logo.png'
html_favicon = '_static/favicon.ico'
html_static_path = ['_static']
html_extra_path = []
pygments_style = 'default'
add_function_parentheses = False
html_show_sourcelink = True
html_show_sphinx = True
html_show_copyright = True
htmlhelp_basename = ''
html_sidebars = {
    'install': ['localtoc.html'],
    'api': ['localtoc.html'],
}

# Theme config
html_theme = 'bootstrap'
html_theme_path = sphinx_bootstrap_theme.get_html_theme_path()
html_theme_options = {
    'navbar_title': html_short_title,
    'navbar_links': [
        ('Install', 'install'),
        ('Gallery', 'gallery/index'),
        ('Tutorial', 'tutorial/index'),
        ('API', 'api'),
        ('Contribute',
         'https://github.com/fatiando/geometric#contributing', True),
        ('<i class="fa fa-github fa-lg" title="Source code on Github"></i>',
         "https://github.com/fatiando/geometric", True),
    ],
    # Render the next and previous page links in navbar. (Default: true)
    'navbar_sidebarrel': False,
    # Render the current pages TOC in the navbar. (Default: true)
    'navbar_pagenav': False,
    # Tab name for the current pages TOC. (Default: "Page")
    'navbar_pagenav_name': "Page",
    # Tab name for entire site. (Default: "Site")
    'navbar_site_name': "Site",
    # Global TOC depth for "site" navbar tab. (Default: 1)
    # Switching to -1 shows all levels.
    'globaltoc_depth': 1,
    # Note: If this is "false", you cannot have mixed ``:hidden:`` and
    # non-hidden ``toctree`` directives in the same page, or else the build
    # will break.
    'globaltoc_includehidden': "false",
    'navbar_class': "navbar navbar-default",
    'navbar_fixed_top': "false",
    'source_link_position': "footer",
    'bootswatch_theme': "flatly",
    'bootstrap_version': "3",
}

# Load the custom CSS files (needs sphinx >= 1.6 for this to work)
def setup(app):
    app.add_stylesheet("style.css")
    app.add_stylesheet('font-awesome/css/font-awesome.css')
