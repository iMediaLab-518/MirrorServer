from utils.cache import cache

from .weather_utils.fetch import get_raw_data
from .weather_utils.match import match
from .weather_utils.save import save


@cache('cache/wind.pkl', 1, 0)
def get_wind():
    raw_data = get_raw_data()
    data = match(raw_data)
    save(data)
    return ' '.join([data['WD'], data['WS']])
