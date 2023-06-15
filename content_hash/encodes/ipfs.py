"""Encode module for IPFS."""

import multihash
from multiformats_cid import make_cid


def encode(value):
    """
    Encode IPFS.

    :param bytes value: a decoded content

    :return: the encoded content
    :rtype: str
    """

    mhash = multihash.from_b58_string(value)
    return make_cid(1, 'dag-pb', mhash).buffer
