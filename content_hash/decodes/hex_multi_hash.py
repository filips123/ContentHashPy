"""Decode module for HEX multi hash."""

import multihash
from multiformats_cid import make_cid


def decode(value):
    """
    Decode HEX multi hash.

    :param bytes value: an encoded content

    :return: the decoded content
    :rtype: str
    """

    cid = make_cid(value)
    return multihash.to_hex_string(multihash.decode(cid.multihash).digest)
