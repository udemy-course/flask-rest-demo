import unittest

from restdemo import create_app, db


class TestBase(unittest.TestCase):

    def setUp(self):
        self.app = create_app(config_name='testing')
        self.client = self.app.test_client
        self.user_data = {
            'username': 'test',
            'password': 'test123',
            'email': 'test@test.com'
        }
        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()
