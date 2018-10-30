import unittest
import requests


class dataTestCase(unittest.TestCase):
    def test_bmi(self):
        req = requests.get("http://localhost:5000/data/BMI")
        self.assertEqual(req.status_code, 200)
        self.assertEqual(req.json()['status'], 100)

    def test_max_heartrate(self):
        req = requests.get("http://localhost:5000/data/max_heartrate")
        self.assertEqual(req.status_code, 200)
        self.assertEqual(req.json()['status'], 100)

    def test_avg_heartrate(self):
        req = requests.get("http://localhost:5000/data/avg_heartrate")
        self.assertEqual(req.status_code, 200)
        self.assertEqual(req.json()['status'], 100)

    def test_MH1(self):
        req = requests.get("http://localhost:5000/data/MH1")
        self.assertEqual(req.status_code, 200)
        self.assertEqual(req.json()['status'], 100)

    def test_MH2(self):
        req = requests.get("http://localhost:5000/data/MH2")
        self.assertEqual(req.status_code, 200)
        self.assertEqual(req.json()['status'], 100)

    def test_weight(self):
        req = requests.get("http://localhost:5000/data/weight")
        self.assertEqual(req.status_code, 200)
        self.assertEqual(req.json()['status'], 100)

    def test_height(self):
        req = requests.get("http://localhost:5000/data/height")
        self.assertEqual(req.status_code, 200)
        self.assertEqual(req.json()['status'], 100)
