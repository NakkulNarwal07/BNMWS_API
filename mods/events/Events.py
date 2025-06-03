from flask import Blueprint, Flask, jsonify
from flask_cors import CORS
from Database import Event



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
    print(event)
    return jsonify(event), 200

