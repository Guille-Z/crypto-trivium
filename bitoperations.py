def limit_mask(bits, n_bits):
    upper_limit = 2 ** n_bits - 1
    masked = bits & upper_limit
    return masked


def pick_bit(bits, position):
    which_bit = 1 << position-1
    picked = bits & which_bit
    picked = picked >> position-1
    return picked


def set_bit(bits, position, value):
    mask = 1 << position-1
    value <<= position-1
    bits = (bits & ~mask) | (value & mask)
    return bits


def dar_vuelta(bits, tam):
    stib = bits
    for i in range(1, tam+1):
        actual = pick_bit(bits, tam-i+1)
        stib = set_bit(stib, i, actual)
    return stib