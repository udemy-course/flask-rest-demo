import json

from restdemo.tests.base import TestBase


class TestUserList(TestBase):

    def test_get_user_list(self):
        # create user
        url = '/user/{}'.format(self.user_data['username'])
        self.client().post(
            url,
            data=self.user_data
        )
        # user login
        url = '/auth/login'
        res = self.client().post(
            url,
            data=json.dumps({'username': 'test', 'password': 'test123'}),
            headers={'Content-Type': 'application/json'}
        )
        res_data = json.loads(res.get_data(as_text=True))
        access_token = '{} {}'.format(
            self.app.config['JWT_AUTH_HEADER_PREFIX'],
            res_data['access_token']
        )
        # get user list
        url = '/users'
        res = self.client().get(
            url,
            headers={'Authorization': access_token}
        )
        res_data = json.loads(res.get_data(as_text=True))
        self.assertEqual(res.status_code, 200)
        self.assertEqual(len(res_data), 1)
