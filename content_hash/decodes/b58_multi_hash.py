"""Decode module for B58 multi hash."""

import multihash
from multiformats_cid import make_cid


def decode(value):
    """
    Decode B58 multi hash.

    :param bytes value: an encoded content

    :return: the decoded content
    :rtype: str
    """

    cid = make_cid(value)
    return multihash.to_b58_string(cid.multihash)
