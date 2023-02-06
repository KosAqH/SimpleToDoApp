from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


db = SQLAlchemy()

app = Flask(__name__, instance_relative_config=False)

app.config['SECRET_KEY'] = 'this-shouldnt-be-here-in-real-app'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

db.init_app(app)

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

from app.models import User, Task

# blueprint for auth routes in our app
from app.auth import auth as auth_blueprint
app.register_blueprint(auth_blueprint)

# blueprint for non-auth parts of app
from app.main import main as main_blueprint
app.register_blueprint(main_blueprint)

with app.app_context():
    db.create_all()