# Flask-VisJS

![PyPI - License](https://img.shields.io/pypi/l/Flask-VisJS)
[![Current version on PyPI](https://img.shields.io/pypi/v/Flask-VisJS)](https://pypi.org/project/Flask-VisJS/)
[![Lint/Build](https://github.com/dadav/Flask-VisJS/actions/workflows/build.yaml/badge.svg)](https://github.com/dadav/Flask-VisJS/actions/)

![Homedir](./img/visjs.png)

Flask-VisJS is a simple wrapper for the famous visjs java library. It helps you to integrate
the library into your flask app.

## Installation

```bash
pip install Flask-VisJS
```

## Example

```python
from flask import Flask, render_template_string
from flask_visjs import VisJS4, Network

app = Flask(__name__)
VisJS4().init_app(app)

@app.route('/')
def index():
    net = Network("500px", "500px")
    net.add_node(0, label="Node 0")
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
```

[Go to the example folder](./examples/)
