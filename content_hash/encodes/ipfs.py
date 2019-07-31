"""Encode module for IPFS."""

from cid import make_cid
import multihash

def encode(value):
    """
    Encode IPFS.

    :param bytes value: a decoded content

    :return: the encoded content
    :rtype: str
    """

    mhash = multihash.from_b58_string(value)
    return make_cid(1, 'dag-pb', mhash).buffer
