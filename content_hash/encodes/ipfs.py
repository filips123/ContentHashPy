"""Encode module for IPFS."""

import base58check
from multiformats_cid import make_cid


def encode(value):
    """
    Encode IPFS.

    :param bytes value: a decoded content

    :return: the encoded content
    :rtype: str
    """

    mhash = base58check.b58decode(value)
    return make_cid(1, 'dag-pb', mhash).buffer
