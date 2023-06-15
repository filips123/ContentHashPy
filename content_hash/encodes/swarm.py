"""Encode module for Swarm."""

from multiformats import multihash, CID
from content_hash.utils import raw_cid_value

def encode(value):
    """
    Encode Swarm.

    :param bytes value: a decoded content

    :return: the encoded content
    :rtype: bytes
    """
    mhash = multihash.wrap(bytes.fromhex(value), 'keccak-256')
    cid = CID(base='base58btc', codec='swarm-manifest', version=1, digest=mhash)
    return raw_cid_value(cid)
