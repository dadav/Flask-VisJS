import pytest
from flask import current_app, Flask
from flask_visjs import VisJS4


@pytest.mark.usefixtures('client')
class TestVisJS4:
    def test_extension_init(self):
        assert 'visjs' in current_app.extensions

    def test_blueprint(self):
        assert 'visjs' in current_app.blueprints

    def test_init_via_class(self):
        app = Flask(__name__)
        VisJS4(app)

    def test_check_if_extensions_key_is_created(self):
        app = Flask(__name__)
        del app.extensions
        VisJS4().init_app(app)
        assert hasattr(app, 'extensions') is True
