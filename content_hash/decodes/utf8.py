"""Decode module for UTF8."""

def decode(value):
    """
    Decode UTF8.

    :param bytes value: an encoded content

    :return: the decoded content
    :rtype: str
    """

    return value.decode('utf-8')
