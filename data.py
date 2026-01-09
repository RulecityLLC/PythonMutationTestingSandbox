# data_layer.py
"""Data access layer - stubbed implementation"""


class UserRepository:
    """Handles data persistence for users"""

    def __init__(self):
        # Stubbed data store
        self._users = {
            1: {"id": 1, "name": "Alice", "email": "alice@example.com"},
            2: {"id": 2, "name": "Bob", "email": "bob@example.com"}
        }
        self._next_id = 3

    def get_all(self):
        """Get all users"""
        return list(self._users.values())

    def get_by_id(self, user_id):
        """Get user by ID"""
        return self._users.get(user_id)

    def create(self, user_data):
        """Create a new user"""
        user_id = self._next_id
        self._next_id += 1

        user = {
            "id": user_id,
            "name": user_data.get("name"),
            "email": user_data.get("email")
        }
        self._users[user_id] = user
        return user