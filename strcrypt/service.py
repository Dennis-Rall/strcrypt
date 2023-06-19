from strcrypt.algorithms import EncodingAlgorithms, ENCODING_ALGORITHMS_MAP, DECODING_ALGORITHMS_MAP, HASHING_ALGORITHMS_MAP, DecodingAlgorithms, HashingAlgorithms


def encode_str(algo: EncodingAlgorithms, s: str) -> str:
    return ENCODING_ALGORITHMS_MAP[algo](s.encode()).decode()

def decode_str(algo: DecodingAlgorithms, s: str) -> str:
    return DECODING_ALGORITHMS_MAP[algo](s.encode()).decode()

def hash_str(algo: HashingAlgorithms, s: str) -> str:
    return HASHING_ALGORITHMS_MAP[algo](s.encode()).hexdigest()

