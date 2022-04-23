from flask import Flask, render_template_string
from flask_visjs import VisJS4, Network

app = Flask(__name__)
VisJS4().init_app(app)

@app.route('/')
def index():
    net = Network("500px", "500px")
    net.add_node(0, label="Node 0")
    net.add_node(1, label="Node 1")
    net.add_edge(0, 1)
    return render_template_string("""
<html>
    <head>
      {{ net.inject_css() }}
    </head>
    <body>
      {{ net.inject_graph() }}
      {{ net.inject_js() }}
    </body>
</html>
""", net=net)
