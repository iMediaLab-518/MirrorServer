import requests
import random


def get_news():
    KEY = "2e4ffe88af8298094690429622bc477d"
    API = "http://v.juhe.cn/toutiao/index?type=top&key={}".format(KEY)
    news = requests.get(API)
    data = news.json()
    titles = [i['title'] for i in data['result']['data']]
    title = random.choice(titles)

    return title


if __name__ == '__main__':
    get_news()
