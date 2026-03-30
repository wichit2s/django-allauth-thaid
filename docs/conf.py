import os
import sys
import django

# Add the project root to the path
sys.path.insert(0, os.path.abspath('..'))

# Initialize Django
os.environ['DJANGO_SETTINGS_MODULE'] = 'tests.settings'
django.setup()

# Project information
project = 'django-allauth-thaid'
copyright = '2026, Wichit Sombat'
author = 'Wichit Sombat'
release = '0.1.0'

# General configuration
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'sphinx.ext.intersphinx',
    'myst_parser',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# HTML output configuration
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# Intersphinx mapping
intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'django': ('https://docs.djangoproject.com/en/stable/', 'https://docs.djangoproject.com/en/stable/_objects/'),
    'allauth': ('https://docs.allauth.org/en/latest/', None),
}

# Auto-doc configurations
autodoc_member_order = 'bysource'
