import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_status_check_endpoint_success(client):
    response = client.get('/status_check')
    assert response.status_code == 200
    data = response.get_json() 
    assert data is not None
    assert data['status'] == 'OK'
    assert 'version' in data