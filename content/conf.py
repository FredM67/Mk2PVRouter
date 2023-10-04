# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import sphinx.ext.mathjax
import zoneinfo

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Documentation du Mk2PVRouter'
copyright = '2023, ENERGIE ROUTER & F. Metrich (aka FredM67)'
author = 'ENERGIE ROUTER & F. Metrich (aka FredM67)'
github_user = "FredM67"
github_repo_name = "Mk2PVRouter"  # auto-detected from dirname if blank
github_version = "main"
conf_py_path = "/content/" # with leading and trailing slash

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    # githubpages just adds a .nojekyll file
    'sphinx.ext.githubpages',
    'sphinx.ext.autosummary',
    'sphinx.ext.todo',
    'sphinx_lesson',
    # 'sphinx.ext.mathjax',
    # 'sphinx-mathjax-offline',
    'sphinx.ext.imgmath',
    'sphinx_rtd_theme_ext_color_contrast',
    'sphinx_copybutton',
    'sphinx_simplepdf',
    'sphinxcontrib.drawio',
    'sphinx.ext.autosectionlabel',
    # 'hoverxref.extension',
    'sphinx_new_tab_link',
    'sphinx_last_updated_by_git',
]
# Make sure the target is unique
autosectionlabel_prefix_document = True

imgmath_image_format = 'svg'
imgmath_embed = True

drawio_builder_export_format = {"simplepdf": "png"}

# hoverxref_roles = [
#     'term',
# ]

git_last_updated_timezone = 'France'

version = "0.1"  # Will not be raised

# Settings for myst_nb:
# https://myst-nb.readthedocs.io/en/latest/use/execute.html#triggering-notebook-execution
nb_execution_mode = "cache"

source_suffix = ['.rst', '.md']

# The master toctree document.
master_doc = "index"

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = [
	"README*",
	"_build",
	"Thumbs.db",
	".DS_Store",
    "jupyter_execute",
    "*venv*",
]

language = 'fr'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = [
    'img/cover.jpg',
]

# HTML context:
from os.path import basename, dirname, realpath
html_context = {
    "display_github": True,
    "github_user": github_user,
    # Auto-detect directory name.  This can break, but
    # useful as a default.
    "github_repo": github_repo_name or basename(dirname(realpath(__file__))),
    "github_version": github_version,
    "conf_py_path": conf_py_path,
}

import os
if os.environ.get('GITHUB_REF', '') == 'refs/heads/'+github_version:
    html_js_files = [
        ('https://plausible.cs.aalto.fi/js/script.js', {"data-domain": "fredm67.github.io", "defer": "defer"}),
    ]

# -- Options for simplepdf output -------------------------------------------------
simplepdf_vars = {
    'primary-opaque': 'rgba(26, 150, 26, 0.7)',
    'cover-bg': 'url(cover.jpg) no-repeat center',
    'primary': '#1a961a',
    'secondary': '#379683',
    'cover': '#ffffff',
    'white': '#ffffff',
    'links': '#1a961a',
    'bottom-center-content:': 'copyright',
}
simplepdf_debug = True

pyppeteer_pdf_options = {
    'printBackground': True,
    'format': 'A4',
    'margin': {
        'top': '20mm',
        'bottom': '20mm',
        'left': '10mm',
        'right': '10mm'
    }
}