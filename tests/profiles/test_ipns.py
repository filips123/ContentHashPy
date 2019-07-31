import content_hash


CODEC = 'ipns-ns'
DECODED = 'QmRAQB6YaCyidP37UdDnjFY5vQuiBrcqdyoW1CuDgwxkD4'
ENCODED = 'e5010170122029f2d17be6139079dc48696d1f582a8530eb9805b561eda517e22a892c7e3f1f'


def test_get_codec():
    assert content_hash.get_codec(ENCODED) == CODEC


def test_decode():
    assert content_hash.decode(ENCODED) == DECODED


def test_encode():
    assert content_hash.encode(CODEC, DECODED) == ENCODED
