from utils.cache import cache

from .weather_utils.fetch import get_raw_data
from .weather_utils.match import match
from .weather_utils.save import save


@cache('cache/pm25.pkl', 1, 0)
def get_pm25():
    raw_data = get_raw_data()
    data = match(raw_data)
    save(data)
    return data['aqi_pm25']
