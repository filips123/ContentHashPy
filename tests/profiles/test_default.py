import content_hash


CODEC = 'onion'
DECODED = 'zqktlwi4fecvo6ri'
ENCODED = 'bc037a716b746c776934666563766f367269'


def test_get_codec():
    assert content_hash.get_codec(ENCODED) == CODEC


def test_decode():
    assert content_hash.decode(ENCODED) == DECODED


def test_encode():
    assert content_hash.encode(CODEC, DECODED) == ENCODED
