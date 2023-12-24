"""Decode module for HEX multi hash."""

import typing

from multiformats import CID, multihash
from multiformats.varint import BytesLike


def decode(value: typing.Union[str, BytesLike]) -> str:
    """
    Decode HEX multi hash.

    :param bytes value: An encoded content
    :return: The decoded content
    """

    return multihash.unwrap(CID.decode(value).digest).hex()
