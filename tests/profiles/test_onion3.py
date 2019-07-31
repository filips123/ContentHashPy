import content_hash


CODEC = 'onion3'
DECODED = 'p53lf57qovyuvwsc6xnrppyply3vtqm7l6pcobkmyqsiofyeznfu5uqd'
ENCODED = 'bd037035336c663537716f7679757677736336786e72707079706c79337674716d376c3670636f626b6d797173696f6679657a6e667535757164'


def test_get_codec():
    assert content_hash.get_codec(ENCODED) == CODEC


def test_decode():
    assert content_hash.decode(ENCODED) == DECODED


def test_encode():
    assert content_hash.encode(CODEC, DECODED) == ENCODED
