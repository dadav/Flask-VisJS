from flask import Flask, render_template_string
from flask_visjs import VisJS4, Network
from pyvis.network import Node
from pathlib import Path

app = Flask(__name__)
VisJS4().init_app(app)


@app.route('/')
def index():
    """
    Network is based on pyvis's network class, you can check out their docs.
    """
    net = Network("1024px", "1024px")
    home = Path.home()
    limit = 250
    current = 0
    for file in home.glob('**/*'):
        if current >= limit:
            break
        net.add_node(str(file), file.name, shape="box" if file.is_file() else "circle")
        net.add_node(str(file.parent), file.parent.name, shape="circle")
        net.add_edge(str(file.parent), str(file))
        current += 1

    return render_template_string("""
<html>
    <head>
      {{ net.inject_css() }}
    </head>
    <body>
      {{ net.inject_js() }}
      {{ net.inject_graph() }}
    </body>
</html>
""", net=net)
