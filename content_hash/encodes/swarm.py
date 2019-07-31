"""Encode module for Swarm."""

from cid import make_cid
import multihash

def encode(value):
    """
    Encode Swarm.

    :param bytes value: a decoded content

    :return: the encoded content
    :rtype: str
    """

    mhash = multihash.encode(multihash.from_hex_string(value), 'keccak-256')
    return make_cid(1, 'swarm-manifest', mhash).buffer
