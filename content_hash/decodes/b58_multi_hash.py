"""Decode module for B58 multi hash."""

from multiformats import multihash
from multiformats_cid import make_cid
from base58check import b58encode

def decode(value):
    """
    Decode B58 multi hash.

    :param bytes value: an encoded content

    :return: the decoded content
    :rtype: str
    """

    cid = make_cid(value)
    return b58encode(cid.multihash)
