"""Encode module for Swarm."""

import multihash
from multiformats_cid import make_cid


def encode(value):
    """
    Encode Swarm.

    :param bytes value: a decoded content

    :return: the encoded content
    :rtype: str
    """

    mhash = multihash.encode(multihash.from_hex_string(value), 'keccak-256')
    return make_cid(1, 'swarm-manifest', mhash).buffer
