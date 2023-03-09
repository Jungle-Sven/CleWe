from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

# initialize the database object
db = SQLAlchemy()
    
def create_app():
    # create the Flask app
    app = Flask(__name__)

    # set the app config
    app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{os.environ['DB_USER']}:{os.environ['DB_PASS']}@{os.environ['DB_HOST']}/{os.environ['DB_NAME']}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app) # initialize the SQLAlchemy object with the Flask app instance

    # import the routes module
    from app import routes

    app.route('/', methods=['GET'])(routes.index)
    app.route('/users', methods=['POST'])(routes.create_user)
    app.route('/users/<int:user_id>', methods=['GET'])(routes.get_user)

    # create all tables
    #with app.app_context():
    #    db.create_all()

    return app
