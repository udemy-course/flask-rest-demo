from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

from restdemo.resource.user import User, UserList
from restdemo.resource.hello import Helloworld


db = SQLAlchemy()


def create_app():

    app = Flask(__name__)
    api = Api(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///demo.db"
    db.init_app(app)

    api.add_resource(Helloworld, '/')
    api.add_resource(User, '/user/<string:username>')
    api.add_resource(UserList, '/users')

    return app
