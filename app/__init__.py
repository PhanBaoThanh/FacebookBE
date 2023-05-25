from flask import Flask
from config import Config

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from flask_socketio import SocketIO


app = Flask(__name__)
app.config.from_object(Config)
cors = CORS(app,resources={r"/*":{"origins":"*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

socketio = SocketIO(app,cors_allowed_origins="*")

if __name__ == '__main__':
    socketio.run(app,debug=True)

from app import socket


from flask_login import LoginManager
login = LoginManager()
login.init_app(app)


db = SQLAlchemy(app)
migrate = Migrate(app, db)

app.app_context().push()

from app import routes
from app import models