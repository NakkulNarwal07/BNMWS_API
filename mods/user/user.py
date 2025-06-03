import os
from flask import Blueprint, Flask, jsonify, request
from flask_cors import CORS
from passlib.hash import argon2
from Database import users, db

user = Blueprint('user', __name__)
CORS(user)

@user.before_request
def apiKeyChecker():
    if request.method == 'OPTIONS':
        # Handle preflight requests by returning an empty response with a 200 status
        return '', 200

    api_key = request.headers.get('x-api-key')
    if api_key != os.environ.get('application_key'):
        return jsonify({'message':'forbidden'}), 403


@user.route('/login/creds', methods=['POST'])
def login():
    try:
        data = request.get_json()
        email = data['email']
        password = data['password']
        cred = users.query.filter_by(email=email).first()

        if cred is None:
            print({"message": "Invalid email or password"})
            return jsonify({"message": "Invalid email or password"}), 400
        else:
            if argon2.verify(password, cred.password_hash):
                # print({"name": cred.name, "email": cred.email, 'image': cred.image})
                return jsonify({'user' : {"name": cred.name, "email": cred.email, 'image': cred.image, 'code': cred.code}}), 200
            else:
                return jsonify({'message': "something went wrong"}), 400

    except Exception as e:
        return jsonify({"message": str(e)}), 400


@user.route('/create_account', methods=['GET', 'POST'])
def create_account():
    try:
        data = request.get_json()
        email = data.get('email')
        name = data.get('name')
        password = data.get('password')
        password_hash =argon2.hash(password)
        Image = data.get('image')
        new_user = users(
            email=email,
            name=name,
            password_hash=password_hash,
            image=Image
        )

        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User created successfully!'}), 201

    except Exception as e:
        print(f"Error storing data: {e}")
        return jsonify({"error": "Failed to store data"}), 500


