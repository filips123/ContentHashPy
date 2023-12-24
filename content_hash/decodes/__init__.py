"""Known decoding functions."""

import importlib
import typing

CACHE: typing.Dict[str, typing.Callable[[bytes], str]] = {}
"""A cache of known decoding functions."""


def get_decode(name: str) -> typing.Callable[[bytes], str]:
    """
    Get decoding function by name.

    Decoding should be a function that takes
    a `bytes` input and returns a `str` result.

    :param name: A decode name
    :return: The resulting decode
    """

    decode = CACHE.get(name)

    if not decode:
        decode = CACHE[name] = importlib.import_module(f".{name}", __name__).decode

    return decode
