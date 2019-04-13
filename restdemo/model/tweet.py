
from sqlalchemy import ForeignKey, func

from restdemo import db
from restdemo.model.base import Base


class Tweet(Base):

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey('user.id'))
    body = db.Column(db.String(140))
    created_at = db.Column(db.DateTime, server_default=func.now())

    def __repr__(self):
        return "user_id={}, tweet={}".format(
            self.user_id, self.body
        )

    def as_dict(self):
        t = {c.name: getattr(self, c.name) for c in self.__table__.columns}
        t['created_at'] = t['created_at'].isoformat()
        return t
