"""Business logic layer"""


class UserService:
    """Handles business logic for users"""

    def __init__(self, repository):
        self.repository = repository

    def get_all_users(self):
        """Get all users with business logic applied"""
        users = self.repository.get_all()
        # Add any business logic here
        return users

    def get_user(self, user_id):
        """Get a specific user"""
        user = self.repository.get_by_id(user_id)
        if not user:
            raise ValueError(f"User with id {user_id} not found")
        return user

    def get_user_by_name(self, name):
        """Get a specific user by name"""
        users = self.repository.get_all()
        matching_users = list(filter(lambda u: u["name"] == name, users))
        if not matching_users:
            raise ValueError(f"User with name {name} not found")
        if len(matching_users) > 1:
            raise ValueError(f"Multiple users with name {name} found")
        return matching_users[0]

    def create_user(self, user_data):
        """Create a new user with validation"""
        # Business logic: validate input
        if not user_data.get("name"):
            raise ValueError("Name is required")
        if not user_data.get("email"):
            raise ValueError("Email is required")

        # Delegate to repository
        return self.repository.create(user_data)
