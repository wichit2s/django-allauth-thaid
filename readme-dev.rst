========================================
django-allauth-thaid contributors
========================================


Build
============

.. code-block::

   uv add django
   uvx --from build pyproject-build


Test
============

create django project and install from 

.. code-block::

   uv python install ./dist/django_allauth_thaid-0.1.0-tar.gz
   uvx pytest


Docs
============

.. code-block::

   uvx sphinx-build -b html docs/ docs/_build/html
