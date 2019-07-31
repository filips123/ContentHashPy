"""Command line program for EIP 1577 content hash."""

# pylint: disable=W0703

import argparse
import sys

from . import get_codec, decode, encode


def handle_get_codec(args):
    """Handle get codec."""

    try:
        chash = args.chash
        codec = get_codec(chash)

    except BaseException as err: # pragma: no cover
        print(str(err), file=sys.stderr)
        sys.exit(1)

    print(codec)


def handle_decode(args):
    """Handle decode."""

    try:
        chash = args.chash
        value = decode(chash)

    except BaseException as err: # pragma: no cover
        print(str(err), file=sys.stderr)
        sys.exit(1)

    print(value)


def handle_encode(args):
    """Handle encode."""

    try:
        codec = args.codec
        value = args.value
        chash = encode(codec, value)

    except BaseException as err: # pragma: no cover
        print(str(err), file=sys.stderr)
        sys.exit(1)

    print(chash)


def main():
    """Handle command line program."""

    parser = argparse.ArgumentParser(
        prog=__package__,
        description='Python implementation of EIP 1577 content hash'
    )
    subparsers = parser.add_subparsers()

    get_codec_parser = subparsers.add_parser(
        name='get-codec',
        help='extract the codec of a content hash'
    )
    get_codec_parser.set_defaults(which='get-codec')
    get_codec_parser.add_argument('chash', help='an hex string containing a content hash')

    get_codec_parser = subparsers.add_parser(
        name='decode',
        help='decode a content hash'
    )
    get_codec_parser.set_defaults(which='decode')
    get_codec_parser.add_argument('chash', help='an hex string containing a content hash')

    get_codec_parser = subparsers.add_parser(
        name='encode',
        help='encode a content hash'
    )
    get_codec_parser.set_defaults(which='encode')
    get_codec_parser.add_argument('codec', help='a codec of a content hash')
    get_codec_parser.add_argument('value', help='a value of a content hash')

    if len(sys.argv) == 1: # pragma: no cover
        parser.print_help(sys.stderr)
        sys.exit(1)

    args = parser.parse_args()

    if args.which == 'get-codec':
        handle_get_codec(args)
    elif args.which == 'decode':
        handle_decode(args)
    elif args.which == 'encode':
        handle_encode(args)


if __name__ == '__main__': # pragma: no cover
    main()
