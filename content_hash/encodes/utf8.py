"""Encode module for UTF8."""

def encode(value):
    """
    Encode UTF8.

    :param bytes value: a decoded content

    :return: the encoded content
    :rtype: str
    """

    return value.encode('utf-8')
