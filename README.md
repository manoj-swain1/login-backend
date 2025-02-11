# Authentication Demo

This is a simple Flask-based web application demonstrating JWT (JSON Web Token) authentication. It includes two main
routes:

1. **Login**: Authenticates users with a username and password, generating a JWT token for valid users.
2. **Validate Session**: Verifies if the session (JWT token) is valid for the logged-in user.

## Features

- **JWT Authentication**: Secure user login and token generation.
- **Role-based Access Control**: Only admins are allowed to login and access the app.
- **Session Validation**: Ensure that the user's session is active by validating the JWT token.

## Requirements

- Python 3.x
- Flask
- Flask-JWT-Extended
- Flask-CORS

## Installation Instructions

1. **Clone the repository**

2. **Install dependencies**:
    ```
    pip install flask flask-cors flask-jwt-extended
    ```

3. **Run the application**:

- Start the Flask app by running:
  ```
  python login.py
  ```

The application will start on `http://localhost:8080`.
