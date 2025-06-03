from flask import Flask, jsonify, request, Blueprint
from Database import Audit, db
import datetime


audit = Blueprint('audit', __name__)

@audit.route('/add/audditLog', methods=["POST"])
def add_auddit_log():
    audit = request.get_json()
    user = audit['user']
    action = audit['action']
    new_audit = Audit(doneby=user, action=action, date_time=datetime.datetime.now())
    db.session.add(new_audit)
    db.session.commit()

    return audit

@audit.route('/', methods=["POST", "GET"])
def add_audit():
    data = Audit.query.all()
    audit = []
    for i in data:
        audit.append({"name": i.doneby, "action": i.action, 'time': i.date_time})
    return jsonify(audit), 200
