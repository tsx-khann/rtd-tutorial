# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'XML Tutorial'
author = 'Khan_32s'
copyright = '2021, xml'
version = '0.1.0'
release = '0.1'

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

html_theme = 'sphinx_rtd_theme'

epub_show_urls = 'footnote'
