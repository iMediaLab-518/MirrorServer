import unittest
import requests


class messageTestCase(unittest.TestCase):
    def test_set(self):
        req = requests.post("http://localhost:5000/message", data={'login': True})
        self.assertEqual(req.status_code, 200)
        self.assertEqual(req.json()['status'], 100)

    def test_get(self):
        req = requests.get("http://localhost:5000/message")
        self.assertEqual(req.status_code, 200)
        self.assertEqual(req.json()['status'], 100)
