from flask import Flask
from Database import db
from flask_cors import CORS
from mods.events.Events import events
from mods.audit.audit import audit
from mods.user.user import user
from  mods.admin.admin import admin
def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config[
        'SQLALCHEMY_DATABASE_URI'] = 'postgresql://avnadmin:AVNS_MIKKB3uW8D-7ngBOEyM@bndatabase-bookn3rd2.j.aivencloud.com:13150/Booknerds?sslmode=require'

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    app.register_blueprint(events, url_prefix='/api/events')
    app.register_blueprint(audit, url_prefix='/api/audit')
    app.register_blueprint(user, url_prefix='/api/user')
    app.register_blueprint(admin, url_prefix='/api/admin')


    return app

app = create_app()
if __name__ == '__main__':
    app.run(port=8080, debug=True)