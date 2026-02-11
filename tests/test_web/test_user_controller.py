"""Tests for UserController"""

import unittest
from unittest.mock import MagicMock
from sample_web_svc.web import UserController
from flask import Flask
import pytest

# app context needed for flask tests
@pytest.fixture(scope="class")
def flask_context_fixture():
    app = Flask(__name__)
    with app.app_context():
        yield

@pytest.mark.usefixtures("flask_context_fixture")
class TestUserController(unittest.TestCase):
    """Unit tests for UserController"""

    def setUp(self):
        self.mock_service = MagicMock()
        self.controller = UserController(self.mock_service)

    def test_get_users_success(self):
        self.mock_service.get_all_users.return_value = [
            {"id": 1, "name": "Alice", "email": "alice@example.com"}
        ]
        response, status_code = self.controller.get_users()
        self.assertEqual(status_code, 200)

        # Get the JSON data from the response
        data = response.get_json()
        self.assertEqual(data, {"users": [{"id": 1, "name": "Alice", "email": "alice@example.com"}]})

        self.mock_service.get_all_users.assert_called_once()

    def test_get_users_error(self):
        self.mock_service.get_all_users.side_effect = Exception("Some error")
        response, status_code = self.controller.get_users()
        self.assertEqual(status_code, 500)
        data = response.get_json()
        self.assertEqual(data, {"error": "Some error"})
        self.mock_service.get_all_users.assert_called_once()

    def test_get_user_success(self):
        expected = {
            "id": 1, "name": "Alice", "email": "alice@example.com"
        }
        self.mock_service.get_user.return_value = expected
        response, status_code = self.controller.get_user(1)
        self.assertEqual(status_code, 200)
        actual = response.get_json()
        self.assertEqual(actual, expected)
        self.mock_service.get_user.assert_called_with(1)

    def test_get_user_not_found(self):
        self.mock_service.get_user.side_effect = ValueError("User not found")
        response, status_code = self.controller.get_user(999)
        self.assertEqual(status_code, 404)
        data = response.get_json()
        self.assertEqual(data, {"error": "User not found"})
