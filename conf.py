# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
import sphinx_pdj_theme
#html_theme = 'sphinx_pdj_theme'
#html_theme_path = [sphinx_pdj_theme.get_html_theme_path()]
import sphinx_rtd_theme
#html_theme = 'sphinx_rtd_theme'

#html_theme = 'yummy_sphinx_theme'

#import sphinx_press_theme
#html_theme = 'press'

html_logo = './_static/logo.jpeg'

import sphinx_bootstrap_theme
html_theme = 'bootstrap'
html_theme_path = ['../lib/python3.5/site-packages/sphinx_bootstrap_theme']
#OPCIONES DE TEMA
#html_theme_options = {'bootswatch_theme': "cosmo"}
#html_theme_options = {'bootswatch_theme': "cerulean"}
html_theme_options = {'bootswatch_theme': "flatly"}

# -- Project information -----------------------------------------------------

project = 'Delta Tracking (Técnico)'
copyright = '2022, Fredy'
author = 'Fredy'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['recommonmark',
 'sphinx_markdown_tables',
 'sphinx.ext.autodoc',
 'sphinx.ext.intersphinx',
 'sphinx.ext.todo',
 'sphinx.ext.mathjax',
 'sphinx.ext.napoleon',
 'sphinx.ext.viewcode'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
#html_theme = 'nature'


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
