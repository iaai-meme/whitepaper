# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'IAAI - meme driven AI blockchain'
copyright = '2024, IA'
author = 'IA, keyboard@iaai.meme'
release = '0.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
html_css_files = ['custom.css']

latex_elements = {
    'papersize': 'a4paper',
    'pointsize': '12pt',
    'preamble': r'''
        \usepackage{helvet}
        \renewcommand{\familydefault}{\sfdefault}
        \usepackage{amsmath,amsfonts,amssymb,amsthm}
        \renewcommand{\normalsize}{\fontsize{12pt}{14pt}\selectfont}
    ''',
}
