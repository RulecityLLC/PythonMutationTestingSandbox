"""Tests for UserRepository"""

import unittest
from src.data import UserRepository


class TestUserRepository(unittest.TestCase):

    def setUp(self):
        self.repo = UserRepository()

    def test_get_all_returns_list(self):
        users = self.repo.get_all()
        self.assertIsInstance(users, list)
        self.assertEqual(len(users), 2)

    def test_get_by_id_existing_user(self):
        user = self.repo.get_by_id(1)
        self.assertIsNotNone(user)
        self.assertEqual(user['id'], 1)
        self.assertEqual(user['name'], 'Alice')

    def test_get_by_id_nonexistent_user(self):
        user = self.repo.get_by_id(999)
        self.assertIsNone(user)

    def test_create_user(self):
        new_user = self.repo.create({
            "name": "Charlie",
            "email": "charlie@example.com"
        })
        self.assertIsNotNone(new_user['id'])
        self.assertEqual(new_user['name'], 'Charlie')
        self.assertEqual(new_user['email'], 'charlie@example.com')
