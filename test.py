import unittest

from server import app


class BasicTests(unittest.TestCase):

    # executed prior to each test
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydb.sqlite3'
        self.app = app.test_client()

        self.assertEqual(app.debug, False)

    # executed after each test
    def tearDown(self):
        pass

    #### tests ####

    def register(self, username, email, password):
        data = dict(username=username, email=email, password=password)
        return self.app.post(
            '/register',
            json=data,
            follow_redirects=True
        )

    def login(self, username, password):
        return self.app.post(
            '/auth',
            json=dict(username=username, password=password),
            follow_redirects=True
        )

    def logout(self):
        return self.app.get(
            '/logout',
            follow_redirects=True
        )

    def test_valid_user_registration(self):
        response = self.register('Testing', 'test@test.com', 'testing')
        print(response.data)
        self.assertEqual(response.status_code, 200)

    def test_valid_user_login(self):
        response = self.login('Testing', 'testing')
        print(response.data)
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
