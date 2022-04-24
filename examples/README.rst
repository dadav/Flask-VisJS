Run the examples
===============

Type these commands in the terminal:

.. code-block:: bash

    $ git clone https://github.com/dadav/Flask-VisJS.git
    $ cd $_
    $ python -m venv venv
    $ source ./venv/bin/activate
    $ pip install pip-tools
    $ pip-sync requirements/examples.txt
    $ cd examples

And the depending on the example you want to run:

A simple network with two nodes:

.. code-block:: bash

    $ FLASK_APP=basic.py flask run

A visualization of your home directory:

.. code-block:: bash

    $ FLASK_APP=home.py flask run

A visualization of your network:

.. code-block:: bash

    $ sudo FLASK_APP=network.py flask run

.. warning::
   Running python as root is dangerous.
   Don't trust me, look at the network.py file first.

Now go to http://localhost:5000.
