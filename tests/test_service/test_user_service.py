"""Tests for UserService"""

import unittest
from unittest.mock import MagicMock
from sample_web_svc.service import UserService


class TestUserService(unittest.TestCase):
    """Unit tests for UserService"""

    def setUp(self):
        self.mock_repo = MagicMock()
        self.service = UserService(self.mock_repo)

    def test_get_all_users(self):
        self.mock_repo.get_all.return_value = [
            {"id": 1, "name": "Alice", "email": "alice@example.com"}
        ]
        users = self.service.get_all_users()
        self.assertEqual(len(users), 1)
        self.mock_repo.get_all.assert_called_once()

    def test_get_user_found(self):
        self.mock_repo.get_by_id.return_value = {
            "id": 1, "name": "Alice", "email": "alice@example.com"
        }
        user = self.service.get_user(1)
        self.assertEqual(user["name"], "Alice")
        self.mock_repo.get_by_id.assert_called_with(1)

    def test_get_user_not_found(self):
        self.mock_repo.get_by_id.return_value = None
        with self.assertRaises(ValueError) as context:
            self.service.get_user(999)
        self.assertEqual("User with id 999 not found", str(context.exception))

    def test_create_user_validation_no_name(self):
        with self.assertRaises(ValueError) as context:
            self.service.create_user({"email": "test@example.com"})
        self.assertEqual("Name is required", str(context.exception))

    def test_create_user_validation_no_email(self):
        with self.assertRaises(ValueError) as context:
            self.service.create_user({"name": "Test"})
        self.assertEqual("Email is required", str(context.exception))

    def test_create_user_success(self):
        self.mock_repo.create.return_value = {
            "id": 3, "name": "Charlie", "email": "charlie@example.com"
        }
        user_data = {
            "name": "Charlie",
            "email": "charlie@example.com"
        }
        user = self.service.create_user(user_data)
        self.assertEqual(user["name"], "Charlie")
        self.mock_repo.create.assert_called_with(user_data)

    def test_get_user_by_name_found(self):
        self.mock_repo.get_all.return_value = [
            {"id": 1, "name": "Alice", "email": "alice@example.com"},
            {"id": 2, "name": "Bob", "email": "bob@example.com"}
        ]
        user = self.service.get_user_by_name("Alice")