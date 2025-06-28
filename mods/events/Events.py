import datetime

from flask import Blueprint, Flask, jsonify, request
from flask_cors import CORS
from Database import Event, db



events = Blueprint('events', __name__)

@events.route('/', methods=['GET', 'POST'])
def home():
    return 'this is home'

@events.route('/getEvents', methods=['GET', 'POST'])
def getEvents():
    data = Event.query.all()
    event = []
    for i in data:
        event.append({"name": i.title, "description": i.description, 'event_date': i.event_date, "location": i.location, 'image_url': i.image})
    # print(event)
    return jsonify(event), 200

@events.route('/addEvent', methods=['GET', 'POST'])
def addEvent():
    data = request.get_json()
    title = data.get('Title')
    # image = data.get('img')
    location = data.get('location')
    desc = data.get('desc')
    date = data.get('date')
    creared_at= datetime.datetime.now()
    new_user = Event(
        name=title,
        image=None,
        location=location,
        desc=desc,
        event_date=date,
        creared_at=creared_at
    )

    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User created successfully!'}), 201