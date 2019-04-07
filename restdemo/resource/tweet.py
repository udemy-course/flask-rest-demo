from flask_restful import Resource, reqparse
from flask_jwt import jwt_required, current_identity

from restdemo.model.user import User as UserModel
from restdemo.model.tweet import Tweet as TweetModel


class Tweet(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'body', type=str, required=True,
        help='body required'
    )

    @jwt_required()
    def post(self, username):
        if current_identity.username != username:
            return {'message': 'please use the right token'}
        user = UserModel.get_by_username(username)
        if not user:
            return {'message': 'user not found'}, 404
        data = Tweet.parser.parse_args()
        tweet = TweetModel(body=data['body'], user_id=user.id)
        tweet.add()
        return {'message': 'post success'}

    @jwt_required()
    def get(self, username):
        user = UserModel.get_by_username(username)
        if not user:
            return {'message': 'user not found'}, 404
        return [t.as_dict() for t in user.tweet]
