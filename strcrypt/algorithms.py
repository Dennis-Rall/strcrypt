from enum import StrEnum
from base64 import (
    a85decode,
    a85encode,
    b16decode,
    b16encode,
    b32decode,
    b32encode,
    b32hexdecode,
    b32hexencode,
    b64decode,
    b64encode,
    b85decode,
    b85encode,
)
from binascii import hexlify, unhexlify
from hashlib import (
    blake2b,
    blake2s,
    md5,
    sha1,
    sha3_224,
    sha3_256,
    sha3_384,
    sha3_512,
    sha224,
    sha256,
    sha384,
    sha512,
)

class HashingAlgorithms(StrEnum):
    BLAKE2B = "blake2b"
    BLAKE2S = "blake2s"
    MD5 = "md5"
    SHA1 = "sha1"
    SHA224 = "sha224"
    SHA256 = "sha256"
    SHA384 = "sha384"
    SHA512 = "sha512"
    SHA3_224 = "sha3_224"
    SHA3_256 = "sha3_256"
    SHA3_384 = "sha3_384"
    SHA3_512 = "sha3_512"


class EncodingAlgorithms(StrEnum):
    A85 = "a85"
    BASE16 = "base16"
    BASE32 = "base32"
    BASE32HEX = "base32hex"
    BASE64 = "base64"
    BASE85 = "base85"
    HEXLIFY = "hexlify"


class DecodingAlgorithms(StrEnum):
    A85 = "a85"
    BASE16 = "base16"
    BASE32 = "base32"
    BASE32HEX = "base32hex"
    BASE64 = "base64"
    BASE85 = "base85"
    HEXLIFY = "hexlify"


ENCODING_ALGORITHMS_MAP = {
    EncodingAlgorithms.A85: a85encode,
    EncodingAlgorithms.BASE16: b16encode,
    EncodingAlgorithms.BASE32: b32encode,
    EncodingAlgorithms.BASE32HEX: b32hexencode,
    EncodingAlgorithms.BASE64: b64encode,
    EncodingAlgorithms.BASE85: b85encode,
    EncodingAlgorithms.HEXLIFY: hexlify,
}


DECODING_ALGORITHMS_MAP = {
    DecodingAlgorithms.A85: a85decode,
    DecodingAlgorithms.BASE16: b16decode,
    DecodingAlgorithms.BASE32: b32decode,
    DecodingAlgorithms.BASE32HEX: b32hexdecode,
    DecodingAlgorithms.BASE64: b64decode,
    DecodingAlgorithms.BASE85: b85decode,
    DecodingAlgorithms.HEXLIFY: unhexlify,
}


HASHING_ALGORITHMS_MAP = {
    HashingAlgorithms.BLAKE2B: blake2b,
    HashingAlgorithms.BLAKE2S: blake2s,
    HashingAlgorithms.MD5: md5,
    HashingAlgorithms.SHA1: sha1,
    HashingAlgorithms.SHA224: sha224,
    HashingAlgorithms.SHA256: sha256,
    HashingAlgorithms.SHA384: sha384,
    HashingAlgorithms.SHA3_224: sha3_224,
    HashingAlgorithms.SHA3_256: sha3_256,
    HashingAlgorithms.SHA3_384: sha3_384,
    HashingAlgorithms.SHA3_512: sha3_512,
    HashingAlgorithms.SHA512: sha512,
}
