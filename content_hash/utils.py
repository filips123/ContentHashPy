"""Util functions used in the project."""

from multiformats import CID, multicodec


def raw_cid_value(cid: CID) -> bytes:
    """Return raw representation of the CID as seen in multiformats_cid in bytes."""

    return b"".join(
        [
            cid.version.to_bytes(1, byteorder="big"),
            multicodec.wrap(cid.codec, cid.digest),
        ],
    )
