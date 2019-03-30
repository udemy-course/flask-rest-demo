from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy()

from restdemo.resource.user import User, UserList
from restdemo.resource.hello import Helloworld


def create_app():

    app = Flask(__name__)
    api = Api(app)
    #app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///demo.db"
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost:3306/demo'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    migrate = Migrate(app, db)

    api.add_resource(Helloworld, '/')
    api.add_resource(User, '/user/<string:username>')
    api.add_resource(UserList, '/users')

    return app
