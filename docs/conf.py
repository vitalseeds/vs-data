"""Sphinx configuration."""
project = "Vs Data"
author = "Tom Readings"
copyright = "2022, Tom Readings"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
