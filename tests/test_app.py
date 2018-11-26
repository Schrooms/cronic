import app
import pytest


@pytest.fixture
def client():
    app.config['TESTING'] = True
    # client = app.test_client()
    yield client


def test_index(client):
    print(dir(app))
    assert False
