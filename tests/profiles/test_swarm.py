import content_hash


CODEC = 'swarm-ns'
DECODED = 'd1de9994b4d039f6548d191eb26786769f580809256b4685ef316805265ea162'
ENCODED = 'e40101fa011b20d1de9994b4d039f6548d191eb26786769f580809256b4685ef316805265ea162'


def test_get_codec():
    assert content_hash.get_codec(ENCODED) == CODEC


def test_decode():
    assert content_hash.decode(ENCODED) == DECODED


def test_encode():
    assert content_hash.encode(CODEC, DECODED) == ENCODED
