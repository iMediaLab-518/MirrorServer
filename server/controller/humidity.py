from ..util import cache

from .weather_utils.fetch import get_raw_data
from .weather_utils.match import match
from .weather_utils.save import save


@cache('cache/humidity.pkl', 1, 0)
def get_humidity():
    raw_data = get_raw_data()
    data = match(raw_data)
    save(data)
    return data['SD']
