"""Encode module for IPFS."""

import base58check
from multiformats import CID, multicodec
from content_hash.utils import raw_cid_value

def encode(value):
    """
    Encode IPFS.

    :param bytes value: a decoded content

    :return: the encoded content
    :rtype: bytes
    """
    mhash = base58check.b58decode(value)
    cid = CID(base='base58btc', codec='dag-pb', version=1, digest=mhash)
    return raw_cid_value(cid)
