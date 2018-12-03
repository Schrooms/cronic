from app import cronic
import pytest


@pytest.fixture
def client():
    cronic.app.config['TESTING'] = True
    # client = app.test_client()
    client = cronic.app.test_client()
    yield client


def test_index(client):
    rv = client.get('/')
    assert b'Index Page' in rv.data


def test_start(client):
    rv = client.post('/start')
    assert b'Start' in rv.data


def test_stop(client):
    rv = client.post('/stop')
    assert b'Stop' in rv.data
