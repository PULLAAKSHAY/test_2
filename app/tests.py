import os
import tempfile
import pytest
from app.app import app, init_db

@pytest.fixture
def client():
    db_fd, app.config['DATABASE'] = tempfile.mkstemp()
    app.config['TESTING'] = True

    with app.test_client() as client:
        with app.app_context():
            init_db()
        yield client

    os.close(db_fd)
    os.unlink(app.config['DATABASE'])

def test_home(client):
    """Test the home page."""
    rv = client.get('/')
    assert rv.status_code == 200

def test_get_messages(client):
    """Test getting messages."""
    rv = client.get('/messages')
    assert rv.status_code == 200
    assert rv.json == []

def test_post_message(client):
    """Test posting a message."""
    rv = client.post('/messages', json={'message': 'Hello, World!'})
    assert rv.status_code == 204

    rv = client.get('/messages')
    assert rv.status_code == 200
    assert rv.json == ['Hello, World!']
