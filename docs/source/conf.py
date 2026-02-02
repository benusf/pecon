import os
import sys

sys.path.insert(0, os.path.abspath("../.."))

project = 'pecon'
copyright = '2026, pecon-devs'
author = 'pecon-devs'
release = '0.1.0'

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.autosummary",
]

autosummary_generate = True
autodoc_default_options = {
    "members": True,
    "undoc-members": False,
    "private-members": False,
}
napoleon_numpy_docstring = True
napoleon_google_docstring = False


html_theme = "pydata_sphinx_theme"

html_logo = "_static/logo.png"

html_theme_options = {
    "logo": {
        "text": "pecon",
    },
    "navbar_end": ["theme-switcher", "version-switcher"],
    "navbar_align": "content",
    "show_version_warning_banner": False,
}

html_context = {
    "version": release,
}

templates_path = ['_templates']
exclude_patterns = []

html_static_path = ['_static']

