"""Known decoding."""

import importlib


CACHE = {}
"""dict: a cache of known decoding"""


def get_decode(name):
    """
    Get decoding function by name.

    Decoding should be a function that takes
    a `bytes` input and returns a `str` result.

    :param str name: a decode name

    :return: the resulting decode
    :rtype: callable
    """

    decode = CACHE.get(name)

    if not decode:
        decode = CACHE[name] = importlib.import_module(f".{name}", __name__).decode

    return decode
