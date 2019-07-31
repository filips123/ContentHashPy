"""Example for EIP 1577 content hash."""

import content_hash


def main():
    """Handle example."""

    # Get codec of content hash
    chash = 'e6013148654c4c6f34757a6a614c65744678364e4833504d774650337162526254663344'
    codec = content_hash.get_codec(chash)
    print('Codec of content hash:', codec)


    # Decode content hash
    chash = 'e6013148654c4c6f34757a6a614c65744678364e4833504d774650337162526254663344'
    address = content_hash.decode(chash)
    print('Decoded content hash:', address)

    # Encode content hash
    address = '1HeLLo4uzjaLetFx6NH3PMwFP3qbRbTf3D'
    chash = content_hash.encode('zeronet', address)
    print('Encoded content hash:', chash)


if __name__ == '__main__':
    main()
