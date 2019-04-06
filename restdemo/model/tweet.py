
from sqlalchemy import ForeignKey, func

from restdemo import db


class Tweet(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey('user.id'))
    body = db.Column(db.String(140))
    created_at = db.Column(db.DateTime, server_default=func.now())

    def __repr__(self):
        return "user_id={}, tweet={}".format(
            self.user_id, self.body
        )
