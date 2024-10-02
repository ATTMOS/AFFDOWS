import os, sys
sys.path.insert(0, os.path.abspath("../.."))
sys.path.append(os.path.abspath("./source"))
sys.path.append(os.path.abspath("./source/user"))

project = 'AFFDO'
copyright = '2024, ATTMOS Inc'
author = 'Madu Manathunga'
release = '24.1.0'

# -- General configuration ---------------------------------------------------
extensions = ["sphinx.ext.todo", "sphinx.ext.viewcode", "sphinx.ext.autodoc", "rst2pdf.pdfbuilder"]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

def setup(app):
    app.add_css_file('custom.css')

# Remove html_baseurl to avoid incorrect absolute paths
# html_baseurl = 'https://attmos.github.io/AFFDOWS'

