import pytest

import content_hash


def test_not_get_nonexistent_codec():
    with pytest.raises(ValueError):
        content_hash.get_codec('0001')


def test_not_decode_nonexistent_codec():
    with pytest.raises(ValueError):
        content_hash.decode('0001')


def test_not_encode_nonexistent_codec():
    with pytest.raises(ValueError):
        content_hash.encode('this-codec-does-not-exist', 'value')
