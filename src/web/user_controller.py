"""API endpoints and request handling"""

from flask import jsonify, request


class UserController:
    """Handles HTTP requests for users"""

    def __init__(self, user_service):
        self.user_service = user_service

    def get_users(self):
        """GET endpoint to retrieve all users"""
        try:
            users = self.user_service.get_all_users()
            return jsonify({"users": users}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    def get_user(self, user_id):
        """GET endpoint to retrieve a specific user"""
        try:
            user = self.user_service.get_user(user_id)
            return jsonify(user), 200
        except ValueError as e:
            return jsonify({"error": str(e)}), 404
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    def create_user(self):
        """POST endpoint to create a new user"""
        try:
            user_data = request.get_json()
            user = self.user_service.create_user(user_data)
            return jsonify(user), 201
        except ValueError as e:
            return jsonify({"error": str(e)}), 400
        except Exception as e:
            return jsonify({"error": str(e)}), 500