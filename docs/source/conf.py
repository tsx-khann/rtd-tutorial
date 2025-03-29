# Configuration file for the Sphinx documentation builder.

# -- Project information
project = 'XML Tutorial'
author = 'Khan_32s'
copyright = '2021, xml'
version = '0.1.0'
release = '0.1'

# -- General configuration
extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}

intersphinx_disabled_domains = ['std']

templates_path = ['_templates']
html_static_path = ['_static']  # Ensure '_static' exists

# -- Options for HTML output
html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'collapse_navigation': True,  # Enables collapsible sidebar menus
    'navigation_depth': 3,  # Ensures deeper levels are visible
}

# -- Options for EPUB output
epub_show_urls = 'footnote'

# -- Master document
master_doc = 'index'  # Ensure it points to the main documentation file
