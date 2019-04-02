from flask_restful import Resource, reqparse

from restdemo import db
from restdemo.model.user import User as UserModel


class Login(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument(
        'password', type=str, required=True,
        help='{error_msg}'
    )
    parser.add_argument(
        'username', type=str, required=True, help='required username'
    )

    def post(self):
        data = Login.parser.parse_args()
        user = db.session.query(UserModel).filter(
            UserModel.username == data['username']
        ).first()
        if user:
            if not user.check_password(data['password']):
                return {
                    "message": "login failed, please input the right username or password"
                }
            return {
                "message": "login success",
                "token": user.generate_token()
            }
        else:
            return {
                "message": "login failed, please input the right username or password"
            }
