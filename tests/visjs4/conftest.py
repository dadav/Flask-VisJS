import pytest
from flask_visjs import VisJS4


@pytest.fixture(autouse=True)
def visjs(app):
    return VisJS4(app)
