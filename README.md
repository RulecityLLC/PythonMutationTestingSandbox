don't merge
# REST API with Layered Architecture
 
A sample REST API built with Flask demonstrating clean architecture principles.
 
## Directory Structure
 
```
project_root/
 ├── src/               # Application source code
 │   ├── data/         # Data access layer (repositories)
 │   ├── service/      # Business logic layer
 │   └── web/          # Web/API layer (controllers)
 ├── tests/            # Test files mirroring src structure
 │   ├── test_data/
 │   ├── test_service/
 │   └── test_web/
 ├── app.py            # Application entry point
 └── requirements.txt  # Python dependencies
 ```
 
## Setup
 
```bash
# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
```

## Running Tests

```bash
# Run all tests
python -m pytest tests/

# Run specific layer tests
python -m pytest tests/test_service/

# Run with coverage
python -m pytest --cov=sample_web_svc tests/
```

## API Endpoints

- `GET /users` - Get all users
- `GET /users/<id>` - Get user by ID
- `POST /users` - Create new user (JSON: {name, email})
- `GET /health` - Health check

## Architecture

- **Data Layer**: Handles data persistence (currently stubbed)
- **Service Layer**: Contains business logic and validation
- **Web Layer**: Handles HTTP requests and responses
- **Dependency Injection**: Layers are wired together in `app.py`
