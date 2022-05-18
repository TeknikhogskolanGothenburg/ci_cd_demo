"""
Unit tests for the API
"""
import json
from src.app import create_app


def test_get_users_status_code():
    """
    Testing status code for get
    :return: None
    """
    app = create_app()

    app.config['TESTING'] = True

    with app.app_context():
        with app.test_client() as api_client:
            response = api_client.get('/api/v1.0/users')
    assert response.status_code == 200


def test_get_users_first_user():
    """
    Testing first user in db
    :return: None
    """
    app = create_app()

    app.config['TESTING'] = True

    with app.app_context():
        with app.test_client() as api_client:
            response = api_client.get('/api/v1.0/users')
    users = json.loads(response.text)
    assert users[0]['first_name'] == 'Alice'
