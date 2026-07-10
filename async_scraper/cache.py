import time


_cache = {}


def get(key):

    data = _cache.get(key)

    if not data:
        return None

    value, expires = data

    if time.time() > expires:
        del _cache[key]
        return None

    return value



def set(key, value, ttl):

    _cache[key] = (
        value,
        time.time() + ttl
    )
