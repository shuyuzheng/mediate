import os
import pytest
from collections.abc import Mapping
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()

    yield client

def test_search(client):
    return client.post('/search', data=dict(
        query="big"
    ), follow_redirects=True)

