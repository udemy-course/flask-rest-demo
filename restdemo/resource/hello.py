from flask_restful import Resource


class Helloworld(Resource):

    def get(self):
        return 'hello world'
