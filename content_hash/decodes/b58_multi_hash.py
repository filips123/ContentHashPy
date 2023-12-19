"""Decode module for B58 multi hash."""

from multiformats import CID
from base58check import b58encode


def decode(value: bytes) -> str:
    """
    Decode B58 multi hash.

    :param value: an encoded content

    :return: the decoded content
    """

    return b58encode(CID.decode(value).digest).decode('utf-8')
