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

## Configuration

There are the following options available:

| Option        | Default           | Description  |
| ------------- | ------------- | ----- |
| VISJS_CDN_TEMPLATE | https://cdnjs.cloudflare.com/ajax/libs/vis/{VERSION}/{FILENAME}' | The CDN to use (only relevant if not localy served) |
| VISJS_JS_FILENAME | vis.min.js | The filename of the javascript file |
| VISJS_CSS_FILENAME | vis.min.css | The filename of the css file |
| VISJS_SERVE_LOCAL | True | If the files should be served localy or from a CDN |
| VISJS_CUSTOM_TEMPLATE_PATH | None | The path for a custom template (used by pyvis) |
| VISJS_VERSION | 4.21.0 (depends on the class) | The version of the visjs library |

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
