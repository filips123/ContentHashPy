"""Python implementation of EIP 1577 content hash."""

from multiformats import multihash, multicodec, CID

from .profiles import get_profile


def decode(chash: str) -> str:
    """
    Decode a content hash.

    :param hash: a hex string containing a content hash

    :return: the decoded content
    """
    codec, raw_data = multicodec.unwrap(bytes.fromhex(chash.lstrip('0x')))
    profile = get_profile(codec.name)
    return profile.decode(raw_data)


def encode(codec: str, value: str) -> str:
    """
    Encode a content hash.

    :param codec: a codec of a content hash
    :param value: a value of a content hash

    :return: the resulting content hash
    """
    value = get_profile(codec).encode(value)
    return multicodec.wrap(codec, value).hex()


def get_codec(chash: str) -> str:
    """
    Extract the codec of a content hash

    :param hash: a hex string containing a content hash

    :return: the extracted codec
    """
    codec, _ = multicodec.unwrap(bytes.fromhex(chash.lstrip('0x')))
    return codec.name
