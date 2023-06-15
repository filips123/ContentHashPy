from multiformats import multicodec

def raw_cid_value(cid):
    """Return raw representation of the CID as seen in multiformats_cid in bytes"""
    return b''.join([cid.version.to_bytes(1, byteorder='big'), multicodec.wrap(cid.codec, cid.digest)])
