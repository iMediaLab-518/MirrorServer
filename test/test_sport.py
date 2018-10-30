import unittest
import requests


class sportTestCase(unittest.TestCase):
    def test_warm_up(self):
        req = requests.get("http://localhost:5000/sport/warmup")
        self.assertEqual(req.status_code, 200)
        self.assertEqual(req.json()['status'], 100)

    def test_start(self):
        req = requests.get("http://localhost:5000/sport/start")
        self.assertEqual(req.status_code, 200)
        self.assertEqual(req.json()['status'], 100)

    def test_sport_times(self):
        req = requests.get("http://localhost:5000/sport/sport_times")
        self.assertEqual(req.status_code, 200)
        self.assertEqual(req.json()['status'], 100)

    def test_calorie(self):
        req = requests.get("http://localhost:5000/sport/calorie")
        self.assertEqual(req.status_code, 200)
        self.assertEqual(req.json()['status'], 100)
