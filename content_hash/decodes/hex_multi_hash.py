"""Decode module for HEX multi hash."""

from multiformats import multihash, CID


def decode(value):
    """
    Decode HEX multi hash.

    :param bytes value: an encoded content

    :return: the decoded content
    :rtype: str
    """
    return multihash.unwrap(CID.decode(value).digest).hex()
