import pytest
import sys
import os
from flask import json


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from main import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_home(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Welcome to Sai chandran's Assessment." in response.data


def test_sanitize_input_sanitized(client):
    response = client.post('/v1/sanitized/input/',
                           data=json.dumps({"input": "safe input"}),
                           content_type='application/json')
    data = json.loads(response.data)
    assert response.status_code == 200
    assert data['result'] == 'sanitized'


def test_sanitize_input_unsanitized(client):
    response = client.post('/v1/sanitized/input/',
                           data=json.dumps({"input": "unsafe input'"}),
                           content_type='application/json')
    data = json.loads(response.data)
    assert response.status_code == 200
    assert data['result'] == 'unsanitized'


def test_no_json(client):
    response = client.post('/v1/sanitized/input/',
                           data="not json", content_type='text/plain')
    data = json.loads(response.data)
    assert response.status_code == 400
    assert data['Error'] == "Invalid Input, Please provide the data in JSON format."


def test_no_input_key(client):
    response = client.post('/v1/sanitized/input/',
                           data=json.dumps({}),
                           content_type='application/json')
    data = json.loads(response.data)
    assert response.status_code == 400
    assert data['Error'] == "No input given."
