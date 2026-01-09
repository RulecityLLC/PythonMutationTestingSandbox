"""Tests for UserController"""

import unittest
from unittest.mock import MagicMock
from src.web import UserController
from flask import Flask
import pytest

# see https://flask.palletsprojects.com/en/stable/appcontext/#creating-an-application-context for the need for this app_context
@pytest.fixture(scope="class")
def flask_context_fixture():
    app = Flask(__name__)
    with app.app_context():
        yield

@pytest.mark.usefixtures("flask_context_fixture")
class TestUserController(unittest.TestCase):

    def setUp(self):
        self.mock_service = MagicMock()
        self.controller = UserController(self.mock_service)

    def test_get_users_success(self):
        self.mock_service.get_all_users.return_value = [
            {"id": 1, "name": "Alice", "email": "alice@example.com"}
        ]
        response, status_code = self.controller.get_users()
        self.assertEqual(status_code, 200)
        self.mock_service.get_all_users.assert_called_once()

    def test_get_user_success(self):
        self.mock_service.get_user.return_value = {
            "id": 1, "name": "Alice", "email": "alice@example.com"
        }
        response, status_code = self.controller.get_user(1)
        self.assertEqual(status_code, 200)

    def test_get_user_not_found(self):
        self.mock_service.get_user.side_effect = ValueError("User not found")
        response, status_code = self.controller.get_user(999)
        self.assertEqual(status_code, 404)