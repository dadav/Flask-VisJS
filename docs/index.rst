Flask-VisJS
===========

Contents
--------

.. toctree::
   :maxdepth: 2

   basic
   examples

Development
-----------

We welcome all kinds of contributions. You can build the development environment
locally with the following commands:

.. code-block:: bash

    $ git clone git@github.com:dadav/Flask-VisJS.git
    $ cd $_
    $ python3 -m venv venv
    $ . venv/bin/activate
    $ pip install pip-tools
    $ pip-sync requirements/dev.txt

Run the tests with pytest:

.. code-block:: bash

    $ pytest

Or run the full checks with tox:

.. code-block:: bash

    $ tox

License
-------

This project is licensed under the MIT License (see the ``LICENSE`` file for
details). Some macros were part of Flask-Bootstrap and were modified under
the terms of its BSD License.
