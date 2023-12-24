"""Encode module for Swarm."""

from multiformats import CID, multihash

from ..utils import raw_cid_value


def encode(value: str) -> bytes:
    """
    Encode Swarm.

    :param value: A decoded content
    :return: The encoded content
    """

    mhash = multihash.wrap(bytes.fromhex(value), "keccak-256")
    cid = CID(base="base58btc", codec="swarm-manifest", version=1, digest=mhash)
    return raw_cid_value(cid)
