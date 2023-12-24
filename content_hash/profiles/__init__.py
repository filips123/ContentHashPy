"""Known decoding and encoding profiles."""

import typing

from ..decodes import get_decode
from ..encodes import get_encode


class Profile:
    """Decoding and encoding profile"""

    __slots__ = ["__encode", "__decode"]

    def __init__(
        self,
        decode: typing.Union[str, typing.Callable[[bytes], str]],
        encode: typing.Union[str, typing.Callable[[str], bytes]],
    ):
        """
        Initialize the class.

        :param decode: A profile decode
        :param encode: A profile encode
        """

        if isinstance(decode, str):
            self.__decode = get_decode(decode)
        elif callable(decode):
            self.__decode = decode
        else:
            raise TypeError("Argument `decode` must be a string or a callable")

        if isinstance(encode, str):
            self.__encode = get_encode(encode)
        elif callable(decode):
            self.__encode = encode
        else:
            raise TypeError("Argument `encode` must be a string or a callable")

    @property
    def decode(self) -> typing.Callable[[bytes], str]:
        """
        Get profile decode.

        :return: The profile decode
        """

        return self.__decode

    @property
    def encode(self) -> typing.Callable[[str], bytes]:
        """
        Get profile encode.

        :return: The profile encode
        """

        return self.__encode


def get_profile(name: str) -> Profile:
    """
    Get profile by name.

    :param name: A profile name
    :return: The profile
    """

    return PROFILES.get(name, PROFILES["default"])


PROFILES = {
    "ipfs": Profile(decode="b58_multi_hash", encode="ipfs"),
    "ipns": Profile(decode="b58_multi_hash", encode="ipfs"),
    "swarm": Profile(decode="hex_multi_hash", encode="swarm"),
    "default": Profile(decode="utf8", encode="utf8"),
}
"""
A dict of known profiles.

`encode` should be chosen among the `encode` modules
`decode` should be chosen among the `decode` modules
"""
