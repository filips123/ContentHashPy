"""Known encoding functions."""

import importlib
import typing

CACHE: typing.Dict[str, typing.Callable[[str], bytes]] = {}
"""A cache of known encoding functions."""


def get_encode(name: str) -> typing.Callable[[str], bytes]:
    """
    Get encoding function by name.

    Encoding should be a function that takes
    a `str` input and returns a `bytes` result.

    :param name: An encode name
    :return: The resulting encode
    """

    encode = CACHE.get(name)

    if not encode:
        encode = CACHE[name] = importlib.import_module(f".{name}", __name__).encode

    return encode
