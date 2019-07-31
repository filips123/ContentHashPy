import pytest

from content_hash.profiles import Profile


def dumb_decode(value):
    return value


def dumb_encode(value):
    return value


def test_profile_with_string():
    profile = Profile(decode='utf8', encode='utf8')

    assert profile.decode.__name__ == 'decode'
    assert profile.encode.__name__ == 'encode'


def test_profile_with_callable():
    profile = Profile(decode=dumb_decode, encode=dumb_encode)

    assert profile.decode.__name__ == 'dumb_decode'
    assert profile.encode.__name__ == 'dumb_encode'


def test_profile_with_other_decode():
    with pytest.raises(TypeError):
        profile = Profile(decode=True, encode='utf8')


def test_profile_with_other_encode():
    with pytest.raises(TypeError):
        profile = Profile(decode='utf8', encode=True)
