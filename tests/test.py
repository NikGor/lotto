import pytest
from flask import url_for
from src.app import app


@pytest.fixture
def client():
    app.config.update(
        TESTING=True,
        WTF_CSRF_ENABLED=False,
        SERVER_NAME='localhost:5000'
    )
    with app.test_client() as client:
        with app.app_context():
            yield client


def test_home(client):
    response = client.get(url_for('home'))
    assert response.status_code == 200


def test_form_submission(client):
    response = client.post(
        url_for('home'),
        data=dict(format=6, from_num=49, tickets=5),
        follow_redirects=True
    )
    assert b'Generated Tickets' in response.data
