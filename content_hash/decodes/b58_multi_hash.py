"""Decode module for B58 multi hash."""

from multiformats import multihash, CID
from base58check import b58encode

def decode(value):
    """
    Decode B58 multi hash.

    :param bytes value: an encoded content

    :return: the decoded content
    :rtype: str
    """
    return b58encode(CID.decode(value).digest)
