# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import sphinx.ext.mathjax

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Mk2PVRouter'
copyright = '2023, ENERGIE ROUTER & F. Metrich (aka FredM67)'
author = 'ENERGIE ROUTER & F. Metrich (aka FredM67)'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    # githubpages just adds a .nojekyll file
    "sphinx.ext.githubpages",
    'myst_parser',
    'sphinx.ext.mathjax',
    'sphinx_rtd_theme_ext_color_contrast',
    'sphinx_copybutton',]

source_suffix = ['.rst', '.md']

templates_path = ['_templates']
exclude_patterns = ['README*', '_build', 'Thumbs.db', '.DS_Store']

language = 'fr'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
# html_static_path = ['_static']
