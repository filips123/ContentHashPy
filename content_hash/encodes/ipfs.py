"""Encode module for IPFS."""

import base58check
from multiformats import CID

from ..utils import raw_cid_value


def encode(value: str) -> bytes:
    """
    Encode IPFS.

    :param value: A decoded content
    :return: The encoded content
    """

    mhash = base58check.b58decode(value)
    cid = CID(base="base58btc", codec="dag-pb", version=1, digest=mhash)
    return raw_cid_value(cid)
