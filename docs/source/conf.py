# Configuration file for the Sphinx documentation builder.

# -- Project Information -----------------------------------------------------

import os
import sys

#project's root directory to sys.path
sys.path.insert(0, os.path.abspath(".."))

# Project information
project = 'XML Tutorial'
copyright = '2024, Your Name'
author = 'Your Name'

# General configuration
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
]

templates_path = ['_templates']
exclude_patterns = []

# HTML output
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# Theme options to collapse sidebar navigation
html_theme_options = {
    "collapse_navigation": True, 
    "navigation_depth": 1, 
}

