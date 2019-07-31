import content_hash


CODEC = 'zeronet'
DECODED = '1HeLLo4uzjaLetFx6NH3PMwFP3qbRbTf3D'
ENCODED = 'e6013148654c4c6f34757a6a614c65744678364e4833504d774650337162526254663344'


def test_get_codec():
    assert content_hash.get_codec(ENCODED) == CODEC


def test_decode():
    assert content_hash.decode(ENCODED) == DECODED


def test_encode():
    assert content_hash.encode(CODEC, DECODED) == ENCODED
