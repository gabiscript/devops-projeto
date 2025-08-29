from app import app

def test_status():
    response = app.test_client().get('/status')
    assert response.status_code == 200
    assert response.get_json()['status'] == "OK"

def test_home():
    response = app.test_client().get('/')
    assert response.status_code == 200
    assert "API da matéria" in response.get_json()['message']

def test_about():
    response = app.test_client().get('/about')
    assert response.status_code == 200
    data = response.get_json()
    assert data['project'] == "DevOps Fase 2"
    assert data['author'] == "Gabi"
