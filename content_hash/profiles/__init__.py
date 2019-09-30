"""Known decoding and encoding profiles."""

from ..decodes import get_decode
from ..encodes import get_encode


class Profile:
    """Decoding and encoding profile"""

    __slots__ = ['__encode', '__decode']

    def __init__(self, decode, encode):
        """
        Initialize the class.

        :param Union[str, callable] decode: a profile decode
        :param Union[str, callable] encode: a profile encode
        """

        if isinstance(decode, str):
            self.__decode = get_decode(decode)
        elif callable(decode):
            self.__decode = decode
        else:
            raise TypeError('Argument `decode` must be a string or a callable')

        if isinstance(encode, str):
            self.__encode = get_encode(encode)
        elif callable(decode):
            self.__encode = encode
        else:
            raise TypeError('Argument `encode` must be a string or a callable')

    @property
    def decode(self):
        """
        Get profile decode.

        :return: the profile decode
        :rtype: callable
        """

        return self.__decode

    @property
    def encode(self):
        """
        Get profile encode.

        :return: the profile encode
        :rtype: str
        """

        return self.__encode


def get_profile(name):
    """
    Get profile by name.

    :param str name: a profile name

    :return: the profile
    :rtype: Profile
    """

    return PROFILES.get(name, PROFILES['default'])


PROFILES = {
    'ipfs-ns': Profile(decode='b58_multi_hash', encode='ipfs'),
    'ipns-ns': Profile(decode='b58_multi_hash', encode='ipfs'),
    'swarm-ns': Profile(decode='hex_multi_hash', encode='swarm'),
    'default': Profile(decode='utf8', encode='utf8'),
}
"""
dict: a dict of known profiles

`encode` should be chosen among the `encode` modules
`decode` should be chosen among the `decode` modules
"""
