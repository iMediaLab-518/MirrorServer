from utils.cache import cache

from .weather_utils.fetch import get_raw_data
from .weather_utils.match import match
from .weather_utils.save import save


@cache('cache/temperature.pkl', 1, 0)
def get_temperature():
    raw_data = get_raw_data()
    data = match(raw_data)
    save(data)
    return data['temp']
