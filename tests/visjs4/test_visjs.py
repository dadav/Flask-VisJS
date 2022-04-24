import pytest
from flask import current_app


@pytest.mark.usefixtures('client')
class TestVisJS4:
    def test_extension_init(self):
        assert 'visjs' in current_app.extensions

    def test_blueprint(self):
        assert 'visjs' in current_app.blueprints
