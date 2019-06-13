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
    bits = (bits & ~mask) | (value & mask);
    return bits
