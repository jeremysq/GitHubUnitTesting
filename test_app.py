# test_hello.py
from app import app
import json
app.config['TESTING'] = True

def test_hello():
    response = app.test_client().get('/')

    assert response.status_code == 200
    assert response.data == b'Hello, World!'

def test_hello_post_work():
    response = app.test_client().post('/', data=json.dumps(dict(key='DockerTest')), content_type='application/json')
    assert response.status_code == 200
    assert response.data == b'Hello, World! This docker is working!'

def test_hello_user_work():
    response = app.test_client().get('/Jeremy')
    assert response.status_code == 200
    assert response.data == b'Hello Jeremy!'

def test_hello_post_fail():
    response = app.test_client().post('/', data=json.dumps(dict(key='DockerFail')), content_type='application/json')
    assert response.status_code == 200
    assert response.data == b'Hello, World! This docker is working!'

def test_hello_user_fail():
    response = app.test_client().get('/Bob')
    assert response.status_code == 200
    assert response.data == b'Hello Jeremy!'