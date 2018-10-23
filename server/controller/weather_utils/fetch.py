import requests


def get_raw_data():
    url = "http://d1.weather.com.cn/sk_2d/101210101.html?_=1538998289736"

    headers = {
        'Host': 'd1.weather.com.cn',
        'Referer': 'http://www.weather.com.cn/weather1d/101210101.shtml',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
    }

    raw_data = requests.get(url, headers=headers).content.decode()
    return raw_data
