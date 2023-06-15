"""Encode module for Swarm."""

from multiformats import multihash
from multiformats_cid import make_cid


def encode(value):
    """
    Encode Swarm.

    :param bytes value: a decoded content

    :return: the encoded content
    :rtype: str
    """

    # mhash = multihash.digest(bytes.fromhex(value), 'keccak-256')
    mhash = multihash.wrap(bytes.fromhex(value), 'keccak-256')
    return make_cid(1, 'swarm-manifest', mhash).buffer
