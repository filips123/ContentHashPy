"""Decode module for UTF8."""


def decode(value: bytes) -> str:
    """
    Decode UTF8.

    :param value: An encoded content
    :return: The decoded content
    """

    return value.decode("utf-8")
