from ..util import cache

from .weather_utils.fetch import get_raw_data
from .weather_utils.match import match
from .weather_utils.save import save


@cache('cache/weather.pkl', 1, 0)
def get_weather():
    raw_data = get_raw_data()
    data = match(raw_data)
    save(data)
    return (data['weather'], data['weathercode'])
