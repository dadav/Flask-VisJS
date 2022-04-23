Basic Usage
===========

Installation
------------

.. code-block:: bash

    $ pip install Flask-VisJS

Initialization
--------------

.. code-block:: python

    from flask_visjs import VisJS4
    from flask import Flask

    app = Flask(__name__)

    VisJS4().init_app(app)


Create a simple network
-----------------------

.. code-block:: python

   from flask_visjs import Network
   my_network = Network()

   # add some data
   my_network.add_node(1, label='First node', shape='box')
   my_network.add_node(2, title='Second node', shape='circle')
   my_network.add_node('third', title='Third node', shape='ellipse')

   # connect the nodes
   my_network.add_edge(1, 2)
   my_network.add_edge(2, 'third', value=2)
   my_network.add_edge('third', 1, title='Foo')

   return render_template('your_template.html.j2', graph=my_network)

Use the network in the template
--------------------------------

.. code-block:: jinja

   <html>
       <head>
         {{ graph.inject_css() }}
       </head>
       <body>
         {{ graph.inject_js() }}
         {{ graph.inject_graph() }}
       </body>
   </html>

Check out the `visjsdocs <https://visjs.github.io/vis-network/docs/network/>`_ for all possible options.

Resources Helpers
-----------------

``graph.inject_css()`` and ``graph.inject_js()``.

Everytime you want to visualize a network, you have to use these helper functions, which add the needed visjs code to your html site.

Run the examples
------------------------

Flask-VisJS provides some example apps which should get you easily started.
See :doc:`examples` for the details.

Configurations
--------------

+----------------------------+-----------------------------------------------------------------------+----------------------------------------------------------------------------------------------+
| Configuration Variable     | Default Value                                                         | Description                                                                                  |
+============================+=======================================================================+==============================================================================================+
| VISJS_CDN_TEMPLATE         | ``'https://cdnjs.cloudflare.com/ajax/libs/vis/{VERSION}/{FILENAME}'`` | The url (with f-string vars) to load the libraries from when the files aren't locally served |
+----------------------------+-----------------------------------------------------------------------+----------------------------------------------------------------------------------------------+
| VISJS_JS_FILENAME          | ``'vis.min.js'``                                                      | The filename of the javascript file which will be used by the ``inject_*`` methods           |
+----------------------------+-----------------------------------------------------------------------+----------------------------------------------------------------------------------------------+
| VISJS_CSS_FILENAME         | ``'vis.min.css'``                                                     | The filename of the css file which will be used by the ``inject_*`` methods                  |
+----------------------------+-----------------------------------------------------------------------+----------------------------------------------------------------------------------------------+
| VISJS_SERVE_LOCAL          | ``True``                                                              | If set to ``True``, local resources will be used for ``inject_*`` methods                    |
+----------------------------+-----------------------------------------------------------------------+----------------------------------------------------------------------------------------------+
| VISJS_CUSTOM_TEMPLATE_PATH | ``None``                                                              | The absolute path to the graph template which will be used by the ``inject_graph`` method    |
+----------------------------+-----------------------------------------------------------------------+----------------------------------------------------------------------------------------------+
| VISJS_VERSION              | ``'4.21.0'``                                                          | The visjs version to use. The default depends on the class you use                           |
+----------------------------+-----------------------------------------------------------------------+----------------------------------------------------------------------------------------------+
