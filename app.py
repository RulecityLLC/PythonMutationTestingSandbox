"""Application entry point with dependency injection"""

from flask import jsonify, Flask
from src.data import UserRepository
from src.service import UserService
from src.web import UserController


def create_app():
    """Factory function to create and configure the Flask app"""
    app_local = Flask(__name__)

    # Dependency injection: wire up the layers
    repository = UserRepository()
    service = UserService(repository)
    controller = UserController(service)

    # Register routes
    @app_local.route('/users', methods=['GET'])
    def get_users():
        return controller.get_users()

    @app_local.route('/users/<int:user_id>', methods=['GET'])
    def get_user(user_id):
        return controller.get_user(user_id)

    @app_local.route('/users', methods=['POST'])
    def create_user():
        return controller.create_user()

    @app_local.route('/health', methods=['GET'])
    def health():
        return jsonify({'status': 'healthy'}), 200

    return app_local


if __name__ == '__main__':
    app = create_app()
    print('Starting server on http://localhost:5000')
    print('Available endpoints:')
    print('  GET  /users - Get all users')
    print('  GET  /users/<id> - Get user by ID')
    print('  POST /users - Create new user (send JSON: {name, email})')
    print('  GET  /health - Health check')
    app.run(debug=True, port=5000)
