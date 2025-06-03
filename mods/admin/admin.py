import os
from flask import Blueprint, Flask, jsonify, request, redirect
from Database import db, users


admin = Blueprint('admin', __name__)

@admin.before_request
def apiKeyChecker():
    if request.method == 'OPTIONS':
        # Handle preflight requests by returning an empty response with a 200 status
        return '', 200

    api_key = request.headers.get('x-api-key')
    if api_key != os.environ.get('application_key'):
        return jsonify({'message':'forbidden'}), 403

@admin.route('/getAll', methods=['GET', 'POST'])
def getAll():
    data = users.query.all()
    allUser = []
    for i in data:
        role = 'Reader'
        if i.code == 'BNADMN07':
            role = 'Admin'
        allUser.append({"email": i.email, "name": i.name, "image": i.image, "role": role})
    return jsonify(allUser), 200



@admin.route('/MakeAdmin/<email>', methods=['PUT'])
def MakeAdmin(email):
    user = users.query.filter_by(email=email).first()
    if user is not None:
        if user.code is None:
            user.code = 'BNADMN07'
        elif user.code == 'BNADMN07':
            user.code = ''

    db.session.commit()

    return jsonify({"message": "Admin has been created"}), 200

@admin.route('/deleteUser/<email>', methods=['DELETE'])
def deleteUser(email):
    user = users.query.filter_by(email=email).first()
    if user:
        db.session.delete(user)
        db.session.commit()

    return jsonify({"message": "User has been deleted"}), 200

@admin.route('/checkAdmin/<email>', methods=['GET'])
def checkAdmin(email):
    cred = users.query.filter_by(email=email).first()
    if cred.code == 'BNADMN07':
         return jsonify({"message": True}), 200
    else:
        return jsonify({"message": False}), 403
