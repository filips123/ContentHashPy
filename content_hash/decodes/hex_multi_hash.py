"""Decode module for HEX multi hash."""

from multiformats import multihash
from multiformats_cid import make_cid


def decode(value):
    """
    Decode HEX multi hash.

    :param bytes value: an encoded content

    :return: the decoded content
    :rtype: str
    """

    cid = make_cid(value)
    return multihash.unwrap(cid.multihash).hex()
