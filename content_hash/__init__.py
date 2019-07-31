"""Python implementation of EIP 1577 content hash."""

import multihash
import multicodec

from .profiles import get_profile


def decode(chash):
    """
    Decode a content hash.

    :param str hash: a hex string containing a content hash

    :return: the decoded content
    :rtype: str
    """

    buffer = multihash.from_hex_string(chash.lstrip('0x'))

    codec = multicodec.get_codec(buffer)
    value = multicodec.remove_prefix(buffer)

    profile = get_profile(codec)
    return profile.decode(value)


def encode(codec, value):
    """
    Encode a content hash.

    :param str codec: a codec of a content hash
    :param str value: a value of a content hash

    :return: the resulting content hash
    :rtype: str
    """

    profile = get_profile(codec)

    value = profile.encode(value)
    value = multicodec.add_prefix(codec, value)
    return multihash.to_hex_string(value)


def get_codec(chash):
    """
    Extract the codec of a content hash

    :param str hash: a hex string containing a content hash

    :return: the extracted codec
    :rtype: str
    """

    buffer = multihash.from_hex_string(chash.lstrip('0x'))
    return multicodec.get_codec(buffer)
