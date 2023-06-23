"""Known encoding."""

import importlib


CACHE = {}
"""dict: a cache of known encoding"""


def get_encode(name):
    """
    Get encoding function by name.

    Encoding should be a function that takes
    a `str` input and returns a `bytes` result.

    :param str name: an encode name

    :return: the resulting encode
    :rtype: callable
    """

    encode = CACHE.get(name)

    if not encode:
        encode = CACHE[name] = importlib.import_module(f".{name}", __name__).encode

    return encode
