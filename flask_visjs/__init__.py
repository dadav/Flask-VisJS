"""
Wrapper for the visjs library
"""
import os
from threading import Lock
from flask import current_app, Blueprint, url_for
from markupsafe import Markup
from pyvis.network import Network as _Network
from flask_visjs._version import __version__


class Network(_Network):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.template_lock = Lock()

    def inject_css(self):
        if current_app.config['VISJS_SERVE_LOCAL']:
            css_url = url_for('visjs.static', filename=current_app.config['VISJS_CSS_FILENAME'])
        else:
            css_url = current_app.config['VISJS_CDN_TEMPLATE'].format(
                VERSION=current_app.config['VISJS_VERSION'],
                FILENAME=current_app.config['VISJS_CSS_FILENAME']
            )
        with self.template_lock:
            path = os.path.join(os.path.dirname(__file__), 'templates', 'pyvis.css.j2')
            self.set_template(path)
            pyvis_plain_css = self.generate_html(notebook=False)
        return Markup(f'<link rel="stylesheet" href="{css_url}"><style>{pyvis_plain_css}</style>')

    def inject_js(self):
        if current_app.config['VISJS_SERVE_LOCAL']:
            js_url = url_for('visjs.static', filename=current_app.config['VISJS_JS_FILENAME'])
        else:
            js_url = current_app.config['VISJS_CDN_TEMPLATE'].format(
                VERSION=current_app.config['VISJS_VERSION'],
                FILENAME=current_app.config['VISJS_JS_FILENAME']
            )

        with self.template_lock:
            path = os.path.join(os.path.dirname(__file__), 'templates', 'pyvis.js.j2')
            self.set_template(path)
            pyvis_plain_js = self.generate_html(notebook=False)
        return Markup(f'<script type="text/javascript" src="{js_url}"></script></br><script type="text/javascript">{pyvis_plain_js}</script>')

    def inject_graph(self):
        with self.template_lock:
            path = current_app.config['VISJS_CUSTOM_TEMPLATE_PATH'] or os.path.join(os.path.dirname(__file__), 'templates', 'pyvis.html.j2')
            self.set_template(path)
            pyvis_plain_graph = self.generate_html(notebook=False)
        return Markup(pyvis_plain_graph)

# def vars2id(*somevars):
#     return ''.join([str(id(v))[:4] for v in somevars])

class _VisJSBase:
    VISJS_VERSION = None

    def __init__(self, app=None):
        self.app = app
        self.version = self.VISJS_VERSION

        if self.app is not None:
            self.init_app(self.app)

    def init_app(self, app):
        app.config.setdefault('VISJS_CDN_TEMPLATE', 'https://cdnjs.cloudflare.com/ajax/libs/vis/{VERSION}/{FILENAME}')
        app.config.setdefault('VISJS_JS_FILENAME', 'vis.min.js')
        app.config.setdefault('VISJS_CSS_FILENAME', 'vis.min.css')
        app.config.setdefault('VISJS_SERVE_LOCAL', True)
        app.config.setdefault('VISJS_CUSTOM_TEMPLATE_PATH', None)
        app.config.setdefault('VISJS_VERSION', self.VISJS_VERSION)

        blueprint = Blueprint('visjs', __name__, static_folder='static', static_url_path='/visjs/static', template_folder='templates')
        app.register_blueprint(blueprint)

        # app.jinja_env.filters['vars2id'] = vars2id

class VisJS4(_VisJSBase):
    VISJS_VERSION = '4.21.0'
