"""Python implementation of EIP 1577 content hash."""

from multiformats import multicodec

from .profiles import get_profile


def decode(chash: str) -> str:
    """
    Decode a content hash.

    :param chash: A hex string containing a content hash
    :return: The decoded content
    """

    codec, raw_data = multicodec.unwrap(bytes.fromhex(chash.lstrip("0x")))
    profile = get_profile(codec.name)
    return profile.decode(raw_data)


def encode(codec: str, value: str) -> str:
    """
    Encode a content hash.

    :param codec: A codec of a content hash
    :param value: A value of a content hash
    :return: The resulting content hash
    """

    value = get_profile(codec).encode(value)
    return multicodec.wrap(codec, value).hex()


def get_codec(chash: str) -> str:
    """
    Extract the codec of a content hash

    :param chash: A hex string containing a content hash
    :return: The extracted codec
    """

    codec, _ = multicodec.unwrap(bytes.fromhex(chash.lstrip("0x")))
    return codec.name
