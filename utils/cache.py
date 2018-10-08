import datetime
import pickle
import os


class CacheExpirationException(Exception):
    '''缓存过期'''


def cache(filepath, h, m):
    def middle(func):
        def wrapper(*args, **kwargs):
            if os.path.exists(filepath):
                try:
                    with open(filepath, 'rb') as f:
                        data = pickle.load(f)
                    now = datetime.datetime.now()
                    last = data['time']

                    delta = h * 60 * 60 + m * 60
                    interval = now - last

                    if interval.days == 0 and interval.total_seconds() <= delta:
                        return data['val']
                    else:
                        raise CacheExpirationException
                except:
                    return func(*args, **kwargs)

        return wrapper

    return middle
