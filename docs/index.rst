The hmp Project
===============

.. toctree::
   :hidden:
   :maxdepth: 1

   license
   reference

My take on the example project for the
`Hypermodern Python <https://cjolowicz.github.io/posts/hypermodern-python-01-setup>`_
article series.
The command-line interface prints random facts to your console
using the `Wikipedia API <https://en.wikipedia.org/api/rest_v1/#/>`_.


Installation
------------

To install the hmp project,
run this command in your terminal:

.. code-block:: console

   $ pip install hmp


Usage
-----

hmp's usage looks like:

.. code-block:: console

   $ hmp [OPTIONS]

.. option:: -l <language>, --language <language>

   The wikipedia language edition,
   as identified by its subdomain on
   `wikipedia.org <https://www.wikipedia.org/>`_.
   By default, the English (en) Wikipedia is selected.

.. option:: --version

   Display the version and exit.

.. option:: --help

   Display a short usage message and exit.
