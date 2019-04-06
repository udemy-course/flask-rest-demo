from datetime import datetime, timedelta

import jwt
from flask import current_app
from werkzeug.security import generate_password_hash, check_password_hash

from restdemo import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    password_hash = db.Column(db.String(128))
    email = db.Column(db.String(64), unique=True)

    def __repr__(self):
        return "id={}, username={}".format(
            self.id, self.username
        )

    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def add(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()
    
    @staticmethod
    def get_by_username(username):
        return db.session.query(User).filter(
            User.username == username
        ).first()
    
    @staticmethod
    def get_by_id(user_id):
        return db.session.query(User).filter(
            User.id == user_id
        ).first()

    @staticmethod
    def get_user_list():
        return db.session.query(User).all()

    @staticmethod
    def authenticate(username, password):
        user = User.get_by_username(username)
        if user:
            # check password
            if user.check_password(password):
                return user

    @staticmethod
    def identity(payload):
        user_id = payload['identity']
        user = User.get_by_id(user_id)
        return user
