from datetime import timedelta
from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'supersecretkey'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(minutes=5)
jwt = JWTManager(app)
CORS(app)

# Simulating a user database
users = {
    "admin": {"password": "admin", "role": "admin"},
    "user": {"password": "user", "role": "user"}
}


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if username in users and users[username]["password"] == password:
        if users[username]["role"] == "admin":
            access_token = create_access_token(identity=username)
            return jsonify({"message": "Login successful", "token": access_token}), 200
        else:
            return jsonify({"message": "Access denied: Admins only"}), 403
    else:
        return jsonify({"message": "Invalid username or password"}), 401


@app.route('/validate-session', methods=['GET'])
@jwt_required()
def is_valid_session():
    current_user = get_jwt_identity()
    if current_user:
        return jsonify({"valid": True}), 200
    return jsonify({"valid": False}), 401


if __name__ == '__main__':
    app.run(port=8080)