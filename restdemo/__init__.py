from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt import JWT

db = SQLAlchemy()

from restdemo.model.user import User as UserModel
from restdemo.resource.user import User, UserList
from restdemo.resource.hello import Helloworld
from restdemo.config import Config

jwt = JWT(None, UserModel.authenticate, UserModel.identity)


def create_app():

    app = Flask(__name__)
    api = Api(app)
    app.config.from_object(Config)
    db.init_app(app)
    migrate = Migrate(app, db)
    jwt.init_app(app)

    api.add_resource(Helloworld, '/')
    api.add_resource(User, '/user/<string:username>')
    api.add_resource(UserList, '/users')
    return app
