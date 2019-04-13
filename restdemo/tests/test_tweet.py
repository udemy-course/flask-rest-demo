import json

from restdemo.tests.base import TestBase


class TestTweet(TestBase):

    def test_tweet(self):
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
        # post tweet
        url = '/tweet/{}'.format(self.user_data['username'])
        res = self.client().post(
            url,
            data={'body': 'hello world'},
            headers={'Authorization': access_token}
        )
        res_data = json.loads(res.get_data(as_text=True))
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res_data, {'message': 'post success'})

        # get tweet
        url = '/tweet/{}'.format(self.user_data['username'])
        res = self.client().get(
            url,
            headers={'Authorization': access_token}
        )
        res_data = json.loads(res.get_data(as_text=True))
        self.assertEqual(res.status_code, 200)
        self.assertEqual(len(res_data), 1)
