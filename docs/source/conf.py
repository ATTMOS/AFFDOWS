# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os, sys
sys.path.insert(0, os.path.abspath("../.."))
#sys.path.append(os.path.abspath("../../src"))
sys.path.append(os.path.abspath("./source"))
sys.path.append(os.path.abspath("./source/user"))
#sys.path.append(os.path.abspath("./source/dev"))

project = 'AFFDO'
copyright = '2024, ATTMOS Inc'
author = 'Madu Manathunga'
release = '24.1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["sphinx.ext.todo", "sphinx.ext.viewcode", "sphinx.ext.autodoc", "rst2pdf.pdfbuilder"]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

def setup(app):
    app.add_css_file('custom.css')

