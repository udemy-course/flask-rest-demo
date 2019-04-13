import unittest
import json

from restdemo import create_app, db


class TestUser(unittest.TestCase):

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

    def test_user_create(self):
        url = '/user/{}'.format(self.user_data['username'])
        res = self.client().post(
            url,
            data=self.user_data
        )
        self.assertEqual(res.status_code, 201)
        res_data = json.loads(res.get_data(as_text=True))
        self.assertEqual(res_data.get('username'), self.user_data['username'])
        self.assertEqual(res_data.get('email'), self.user_data['email'])

        res = self.client().post(
            url,
            data=self.user_data
        )
        self.assertEqual(res.status_code, 200)
        res_data = json.loads(res.get_data(as_text=True))
        self.assertEqual(res_data.get('message'), 'user already exist')

    def test_user_get(self):
        url = '/user/{}'.format(self.user_data['username'])
        res = self.client().post(
            url,
            data=self.user_data
        )
        res = self.client().get(url)
        res_data = json.loads(res.get_data(as_text=True))
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res_data.get('username'), self.user_data['username'])
        self.assertEqual(res_data.get('email'), self.user_data['email'])

    def test_user_get_not_exist(self):
        url = '/user/{}'.format(self.user_data['username'])
        res = self.client().get(url)
        res_data = json.loads(res.get_data(as_text=True))
        self.assertEqual(res.status_code, 404)
        self.assertEqual(res_data, {'message': 'user not found'})

    def test_user_delete(self):
        url = '/user/{}'.format(self.user_data['username'])
        self.client().post(
            url,
            data=self.user_data
        )
        res = self.client().delete(url)
        res_data = json.loads(res.get_data(as_text=True))
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res_data, {'message': 'user deleted'})

    def test_user_delete_not_exist(self):
        url = '/user/{}'.format(self.user_data['username'])
        res = self.client().delete(url)
        res_data = json.loads(res.get_data(as_text=True))
        self.assertEqual(res.status_code, 404)
        self.assertEqual(res_data, {'message': 'user not found'})

    def test_user_update(self):
        url = '/user/{}'.format(self.user_data['username'])
        self.client().post(
            url,
            data=self.user_data
        )
        res = self.client().put(
            url,
            data={
                'password': 'newpassword',
                'email': 'newemail@new.com'
            }
        )
        res_data = json.loads(res.get_data(as_text=True))
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res_data['email'], 'newemail@new.com')

    def test_user_update_not_exist(self):
        url = '/user/{}'.format(self.user_data['username'])
        res = self.client().put(
            url,
            data={
                'password': 'newpassword',
                'email': 'newemail@new.com'
            }
        )
        res_data = json.loads(res.get_data(as_text=True))
        self.assertEqual(res.status_code, 404)
        self.assertEqual(res_data, {'message': 'user not found'})
