import numpy as np
def bytes_to_bits(data: bytes):
    return np.unpackbits(
        np.frombuffer(data, dtype=np.uint8)
    )
def bits_to_bytes(bits):
    bits = np.asarray(bits, dtype=np.uint8)
    return np.packbits(bits).tobytes()