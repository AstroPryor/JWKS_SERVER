import unittest
import json
from app import app

class JWKSTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_jwks(self):
        response = self.app.get('/.well-known/jwks.json')
        self.assertEqual(response.status_code, 200)
        keys = json.loads(response.data)
        self.assertIn("keys", keys)

    def test_auth(self):
        response = self.app.post('/auth')
        self.assertEqual(response.status_code, 200)
        token = json.loads(response.data)["token"]
        self.assertIsNotNone(token)

    def test_auth_expired(self):
        response = self.app.post('/auth?expired=true')
        self.assertEqual(response.status_code, 200)
        token = json.loads(response.data)["token"]
        self.assertIsNotNone(token)

if __name__ == '__main__':
    unittest.main()
