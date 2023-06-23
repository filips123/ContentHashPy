ContentHash for Python
======================

[![version][icon-version]][link-pypi]
[![downloads][icon-downloads]][link-pypi]
[![license][icon-license]][link-license]
[![python][icon-python]][link-python]

[![build][icon-build]][link-build]
[![coverage][icon-coverage]][link-coverage]
[![quality][icon-quality]][link-quality]

Python implementation of EIP 1577 content hash.

## Description

This is a simple package made for encoding and decoding content hashes has specified in the [EIP 1577][link-eip-1577].
This package will be useful for every [Ethereum][link-ethereum] developer wanting to interact with [EIP 1577][link-eip-1577] compliant [ENS resolvers][link-resolvers].

For JavaScript implementation, see [`pldespaigne/content-hash`][link-javascript-implementation].

## Installation

### Requirements

ContentHash requires Python 3.5 or higher.

### From PyPI

The recommended way to install ContentHash is from PyPI with PIP.

```bash
pip install content-hash
```

### From Source

Alternatively, you can also install it from the source.

```bash
git clone https://github.com/filips123/ContentHashPy.git
cd ContentHashPy
python setup.py install
```

## Usage

### Supported Codecs

The following codecs are currently supported:

- `swarm-ns`
- `ipfs-ns`
- `ipns-ns`

Every other codec supported by [`multicodec`][link-multicodec] will be encoded by default in `utf-8`. You can see the full list of the supported codecs [here][link-supported-codecs].

### Getting Codec

You can use a `get_codec` function to get codec from the content hash.

It takes a content hash as a HEX string and returns the codec name. A content hash can be prefixed with a `0x`, but it's not mandatory.

```py
import content_hash

chash = 'bc037a716b746c776934666563766f367269'
codec = content_hash.get_codec(chash)

print(codec) # onion
```

### Decoding

You can use a `decode` function to decode a content hash.

It takes a content hash as a HEX string and returns the decoded content as a string. A content hash can be prefixed with a `0x`, but it's not mandatory.

```py
import content_hash

chash = 'e3010170122029f2d17be6139079dc48696d1f582a8530eb9805b561eda517e22a892c7e3f1f'
value = content_hash.decode(chash)

print(value) # QmRAQB6YaCyidP37UdDnjFY5vQuiBrcqdyoW1CuDgwxkD4
```

### Encoding

You can use an `encode` function to encode a content hash.

It takes a supported codec as a string and a value as a string and returns the corresponding content hash as a HEX string. The output will not be prefixed with a `0x`.

```py
import content_hash

codec = 'swarm-ns'
value = 'd1de9994b4d039f6548d191eb26786769f580809256b4685ef316805265ea162'
chash = content_hash.encode(codec, value)

print(chash) # e40101701b20d1de9994b4d039f6548d191eb26786769f580809256b4685ef316805265ea162
```

## Creating Codecs

All supported codec profiles are available in [`content_hash/profiles/__init__.py`][link-profiles-file], in `PROFILES` dictionary. You need to add a new profile there. You only need to add a new profile if your codec encoding and decoding are different from `utf-8`.

Each profile must have the same name as the corresponding codec in the `multicodec` library.

A profile must also have decode and encode function. They should be passed as a string containing the name of the module for required decode or encode. All such modules are available in [`content_hash/decodes`][link-decodes-directory] and [`content_hash/encodes`][link-encodes-directory].

Each module name should describe it as much as possible. Its name can only contain valid characters for Python modules.

Each decode module must have a `decode` function. It must be a function that takes a `bytes` input and returns a `str` result.

Each encode module must have an `encode` function. It must be a function that takes a `str` input and returns a `bytes` result.

All inputs and outputs must be the same as in the [JavaScript implementation][link-javascript-implementation]. Multiple profiles can share the same decodes and encodes.

## Versioning

This library uses [SemVer][link-semver] for versioning. For the versions available, see [the tags][link-tags] on this repository.

## License

This library is licensed under the MIT license. See the [LICENSE][link-license-file] file for details.

[icon-version]: https://img.shields.io/pypi/v/content-hash.svg?style=flat-square&label=version
[icon-downloads]: https://img.shields.io/pypi/dm/content-hash.svg?style=flat-square&label=downloads
[icon-license]: https://img.shields.io/pypi/l/content-hash.svg?style=flat-square&label=license
[icon-python]: https://img.shields.io/pypi/pyversions/content-hash?style=flat-square&label=python

[icon-build]: https://img.shields.io/github/actions/workflow/status/filips123/ContentHashPy/main.yml?style=flat-square&label=build
[icon-coverage]: https://img.shields.io/scrutinizer/coverage/g/filips123/ContentHashPy.svg?style=flat-square&label=coverage
[icon-quality]: https://img.shields.io/scrutinizer/g/filips123/ContentHashPy.svg?style=flat-square&label=quality

[link-pypi]: https://pypi.org/project/content-hash/
[link-license]: https://choosealicense.com/licenses/mit/
[link-python]: https://python.org/
[link-build]: https://github.com/filips123/ContentHashPy/actions
[link-coverage]: https://scrutinizer-ci.com/g/filips123/ContentHashPy/code-structure/
[link-quality]: https://scrutinizer-ci.com/g/filips123/ContentHashPy/
[link-semver]: https://semver.org/

[link-eip-1577]: https://github.com/ethereum/EIPs/blob/master/EIPS/eip-1577.md
[link-ethereum]: https://www.ethereum.org/
[link-resolvers]: http://docs.ens.domains/en/latest/introduction.html
[link-multicodec]: https://github.com/multiformats/multicodec/
[link-supported-codecs]: https://github.com/multiformats/multicodec/blob/master/table.csv

[link-tags]: https://github.com/filips123/ContentHashPy/tags/
[link-license-file]: https://github.com/filips123/ContentHashPy/blob/master/LICENSE
[link-profiles-file]: https://github.com/filips123/ContentHashPy/blob/master/content_hash/profiles/__init__.py
[link-decodes-directory]: https://github.com/filips123/ContentHashPy/tree/master/content_hash/decodes/
[link-encodes-directory]: https://github.com/filips123/ContentHashPy/tree/master/content_hash/encodes/

[link-javascript-implementation]: https://github.com/pldespaigne/content-hash/
