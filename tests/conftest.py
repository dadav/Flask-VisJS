import pytest
from flask import Flask


@pytest.fixture(autouse=True)
def app():
    app = Flask(__name__)
    app.testing = True
    app.secret_key = 'test'

    @app.route('/')
    def index():
        return 'Test'

    yield app


@pytest.fixture
def client(app):
    context = app.test_request_context()
    context.push()

    with app.test_client() as client:
        yield client

    context.pop()
