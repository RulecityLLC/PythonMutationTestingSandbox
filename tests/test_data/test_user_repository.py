"""Tests for UserRepository"""

import unittest
from sample_web_svc.data import UserRepository


class TestUserRepository(unittest.TestCase):
    """Unit tests to User Repository"""

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
        self.assertEqual(user['email'], 'alice@example.com')

    def test_get_by_id_existing_user2(self):
        user = self.repo.get_by_id(2)
        self.assertIsNotNone(user)
        self.assertEqual(user['id'], 2)
        self.assertEqual(user['name'], 'Bob')
        self.assertEqual(user['email'], 'bob@example.com')

    def test_get_by_id_nonexistent_user(self):
        user = self.repo.get_by_id(999)
        self.assertIsNone(user)

    def test_create_users(self):
        new_user = self.repo.create({
            'name': 'Charlie',
            'email': 'charlie@example.com'
        })
        self.assertEqual(new_user['id'], 3)
        self.assertEqual(new_user['name'], 'Charlie')
        self.assertEqual(new_user['email'], 'charlie@example.com')

        new_user = self.repo.create({
            'name': 'Bill',
            'email': 'bill@example.com'
        })
        self.assertEqual(new_user['id'], 4)
        self.assertEqual(new_user['name'], 'Bill')
        self.assertEqual(new_user['email'], 'bill@example.com')

    def test_create_user(self):
        new_user = self.repo.create({
            'name': 'Charlie',
            'email': 'charlie@example.com'
        })
        self.assertEqual(new_user['id'], 3)
        self.assertEqual(new_user['name'], 'Charlie')
        self.assertEqual(new_user['email'], 'charlie@example.com')

        user = self.repo.get_by_id(3)
        self.assertIsNotNone(user)
