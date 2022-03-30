Quickstart Guide
================

Requirements
------------

Install Cookiecutter_:

.. code:: console

   $ pipx install cookiecutter

Install Poetry_ by downloading and running install-poetry.py_:

.. _install-poetry.py: https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py

.. code:: console

   $ python install-poetry.py

Install Nox_ and nox-poetry_:

.. code:: console

   $ pipx install nox
   $ pipx inject nox nox-poetry

pipx_ is preferred, but you can also install with ``pip install --user``.

It is recommended to set up Python 3.7, 3.8, 3.9, 3.10 using pyenv_.


Creating a project
------------------

Generate a Python project:

.. code:: console

   $ cookiecutter gh:lucasad83/digit-skeleton-cookiecutter

Change to the root directory of your new project,
and create a Git repository:

.. code:: console

   $ git init
   $ git add .
   $ git commit


Running
-------

Run the command-line interface from the source tree:

.. code:: console

   $ poetry install
   $ poetry run <project>

Run an interactive Python session:

.. code:: console

   $ poetry install
   $ poetry run python


Testing
-------

Run the full test suite:

.. code:: console

   $ nox

List the available Nox sessions:

.. code:: console

   $ nox --list-sessions

Install the pre-commit hooks:

.. code:: console

   $ nox -s pre-commit -- install


Releasing
---------

Releases are triggered by a version bump on the default branch.
It is recommended to do this in a separate pull request:

1. Switch to a branch.
2. Bump the version using `poetry version`_.
3. Commit and push.
4. Open a pull request.
5. Merge the pull request.

.. _poetry version: https://python-poetry.org/docs/cli/#version

The Release workflow performs the following automated steps:

- Build and upload the package.
- Apply a version tag to the repository.
- Publish a release.

Release notes are populated with the titles and authors of merged pull requests.
You can group the pull requests into separate sections
by applying labels to them, like this:

.. table-release-drafter-sections-begin

.. table::
   :class: table
   :widths: auto

   =================== ============================
   Pull Request Label  Section in Release Notes
   =================== ============================
   ``breaking``        💥 Breaking Changes
   ``enhancement``     🚀 Features
   ``removal``         🔥 Removals and Deprecations
   ``bug``             🐞 Fixes
   ``performance``     🐎 Performance
   ``testing``         🚨 Testing
   ``ci``              👷 Continuous Integration
   ``documentation``   📚 Documentation
   ``refactoring``     🔨 Refactoring
   ``style``           💄 Style
   ``dependencies``    📦 Dependencies
   =================== ============================

.. table-release-drafter-sections-end

.. include:: ../README.rst
   :start-after: references-begin
   :end-before: references-end

.. quickstart-references-begin

.. _GitHub: https://github.com/
.. _nox-poetry: https://nox-poetry.readthedocs.io/
.. _pipx: https://pipxproject.github.io/pipx/
.. _pyenv: https://github.com/pyenv/pyenv

.. quickstart-references-end
