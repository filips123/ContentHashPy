"""Python implementation of EIP 1577 content hash."""

from multiformats import multicodec

from .profiles import get_profile


def decode(chash):
    """
    Decode a content hash.

    :param str hash: a hex string containing a content hash

    :return: the decoded content
    :rtype: str
    """
    buffer = bytes.fromhex(chash.lstrip('0x'))

    codec, value = multicodec.unwrap(buffer)
    profile = get_profile(codec.name)
    result = profile.decode(value)
    if isinstance(result, bytes):
        result = result.decode()
    return result


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
    value = multicodec.wrap(codec, value)
    return value.hex()


def get_codec(chash):
    """
    Extract the codec of a content hash

    :param str hash: a hex string containing a content hash

    :return: the extracted codec
    :rtype: str
    """

    buffer = bytes.fromhex(chash.lstrip('0x'))
    codec, _ =  multicodec.unwrap(buffer)
    return codec.name
