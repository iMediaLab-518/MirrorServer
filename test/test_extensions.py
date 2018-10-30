import unittest
import requests


class extensionsTestCase(unittest.TestCase):
    def test_humidity(self):
        req = requests.get("http://localhost:5000/humidity")
        self.assertEqual(req.status_code, 200)
        self.assertEqual(req.json()['status'], 100)

    def test_temperature(self):
        req = requests.get("http://localhost:5000/temperature")
        self.assertEqual(req.status_code, 200)
        self.assertEqual(req.json()['status'], 100)

    def test_heartrate(self):
        req = requests.get("http://localhost:5000/heartrate")
        self.assertEqual(req.status_code, 200)
        self.assertEqual(req.json()['status'], 100)

    def test_traveladvice(self):
        req = requests.get("http://localhost:5000/traveladvice")
        self.assertEqual(req.status_code, 200)
        self.assertEqual(req.json()['status'], 100)

    def test_news(self):
        req = requests.get("http://localhost:5000/news")
        self.assertEqual(req.status_code, 200)
        self.assertEqual(req.json()['status'], 100)

    def test_pm25(self):
        req = requests.get("http://localhost:5000/pm25")
        self.assertEqual(req.status_code, 200)
        self.assertEqual(req.json()['status'], 100)

    def test_weather(self):
        req = requests.get("http://localhost:5000/weather")
        self.assertEqual(req.status_code, 200)
        self.assertEqual(req.json()['status'], 100)

    def test_wind(self):
        req = requests.get("http://localhost:5000/wind")
        self.assertEqual(req.status_code, 200)
        self.assertEqual(req.json()['status'], 100)
