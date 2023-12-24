"""Decode module for B58 multi hash."""

import typing

from base58check import b58encode
from multiformats import CID
from multiformats.varint import BytesLike


def decode(value: typing.Union[str, BytesLike]) -> str:
    """
    Decode B58 multi hash.

    :param value: An encoded content
    :return: The decoded content
    """

    return b58encode(CID.decode(value).digest).decode("utf-8")
