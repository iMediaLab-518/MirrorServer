import unittest
import requests


class authTestCase(unittest.TestCase):
    def test_login(self):
        req = requests.get("http://localhost:5000/login")
        self.assertEqual(req.status_code, 200)
        self.assertEqual(req.json()['status'], 100)
