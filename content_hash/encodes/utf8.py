"""Encode module for UTF8."""


def encode(value: str) -> bytes:
    """
    Encode UTF8.

    :param value: A decoded content
    :return: The encoded content
    """

    return value.encode("utf-8")
