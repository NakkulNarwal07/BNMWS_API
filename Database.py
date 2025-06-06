from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

class users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    name = db.Column(db.String(255))
    image = db.Column(db.String(255))
    code = db.Column(db.String(255))
    password_hash = db.Column(db.Text)
    oauth_provider = db.Column(db.String(50))
    oauth_provider_id = db.Column(db.String(255))
    created_at = db.Column(db.DateTime(timezone=True))
    updated_at = db.Column(db.DateTime(timezone=True))

class Audit(db.Model):
    __tablename__ = 'audit'  # Name of the table in the database
    date_time = db.Column(db.DateTime(timezone=True), nullable=False)
    audit_id = db.Column(db.Integer, primary_key=True)  # Primary Key
    doneby = db.Column(db.String(50), nullable=False)  # User who performed the action
    action = db.Column(db.String(255), nullable=False)  # Action performed

class Event(db.Model):
    __tablename__ = 'events'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    event_date = db.Column(db.Date, nullable=False)
    location = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    image = db.Column(db.String(255))
