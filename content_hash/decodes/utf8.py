"""Decode module for UTF8."""

def decode(value: bytes) -> str:
    """
    Decode UTF8.

    :param value: an encoded content

    :return: the decoded content
    """

    return value.decode('utf-8')
