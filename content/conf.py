# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import sphinx.ext.mathjax

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
    'sphinx_lesson',
    'sphinx.ext.mathjax',
    'sphinx-mathjax-offline',
    'sphinx.ext.imgmath',
    'sphinx_rtd_theme_ext_color_contrast',
    'sphinx_copybutton',
    'sphinx_simplepdf',
]

imgmath_image_format = 'svg'
imgmath_embed = True

# Settings for myst_nb:
# https://myst-nb.readthedocs.io/en/latest/use/execute.html#triggering-notebook-execution
nb_execution_mode = "cache"

source_suffix = ['.rst', '.md']

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
# html_static_path = ['_static']
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
