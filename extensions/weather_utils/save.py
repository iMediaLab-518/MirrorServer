'''

数据格式类似于：
{'nameen': 'hangzhou', 'cityname': '杭州', 'city': '101210101', 'temp': '21', 'tempf': '69', 'WD': '东北风', 'wde': 'NE', 'WS': '2级', 'wse': '&lt;12km/h', 'SD': '77%', 'time': '20:00', 'weather': '多云', 'weathere': 'Cloudy', 'weathercode': 'n01', 'qy': '1016', 'njd': '暂缺', 'sd': '77%', 'rain': '0.0', 'rain24h': '0', 'aqi': '46', 'limitnumber': '1和9', 'aqi_pm25': '46', 'date': '10月08日(星期一)'}



'''

import pickle
import datetime


def _add_time(data):
    return {
        'val': data,
        'time': datetime.datetime.now()
    }


def _save_file(filename, data):
    data = _add_time(data)
    with open(filename, 'wb') as f:
        pickle.dump(data, f)


def save(weather_data):
    temperature = weather_data['temp']
    wind = ' '.join([weather_data['WD'], weather_data['WS']])
    humidity = weather_data['SD']
    weather = weather_data['weather']
    pm25 = weather_data['aqi_pm25']

    _save_file('cache/temperature.pkl', temperature)
    _save_file('cache/wind.pkl', wind)
    _save_file('cache/humidity.pkl', humidity)
    _save_file('cache/weather.pkl', weather)
    _save_file('cache/pm25.pkl', pm25)
