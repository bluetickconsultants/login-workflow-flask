import unittest
from app import app, db

class AuthenticationTestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_register(self):
        data = {
            'email': 'test@example.com',
            'password': 'testpassword'
        }
        response = self.app.post('/register', json=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"message": "User created successfully"})

    def test_login(self):
        data = {
            'email': 'test@example.com',
            'password': 'testpassword'
        }
        self.app.post('/register', json=data)
        response = self.app.post('/login', json=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('token', response.json)
        self.assertIn('user_id', response.json)

if __name__ == '__main__':
    unittest.main()
