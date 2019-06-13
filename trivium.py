from bitoperations import *


class Trivium:
    __key_length = 80
    __iv_length = 80
    __state_length = 288
    __iterations = 4
    __max_bits = 2**64

    def __init__(self, key, iv):
        self.__state = 0
        self.__key = key
        self.__iv = iv

        # === Key and IV Setup (2.2 Paper) ===
        self.__state |= self.__key          # s1..s80..s93
        self.__state |= (self.__iv << 93)   # s94....s177
        self.__state |= 7 << 285            # s286, s287, s288
        # Initial 4 iterations
        for i in range(2*288):
            t1 = pick_bit(self.__state, 66) ^ pick_bit(self.__state, 91) & pick_bit(self.__state, 92) ^\
                pick_bit(self.__state, 93) ^ pick_bit(self.__state, 171)
            t2 = pick_bit(self.__state, 162) ^ pick_bit(self.__state, 175) & pick_bit(self.__state, 176) ^ \
                pick_bit(self.__state, 177) ^ pick_bit(self.__state, 264)
            t3 = pick_bit(self.__state, 243) ^ pick_bit(self.__state, 286) & pick_bit(self.__state, 287) ^ \
                pick_bit(self.__state, 288) ^ pick_bit(self.__state, 69)
            # Shifting and ditching last bit
            self.__state <<= 1
            self.__state = limit_mask(self.__state, 288)
            # Updating new values
            self.__state = set_bit(self.__state, 1, t3)
            self.__state = set_bit(self.__state, 94, t1)
            self.__state = set_bit(self.__state, 178, t2)
        print("0x%X" % self.__state)

    def __keystream(self):
        # Key Stream Generation (2.1 Paper)
        for i in range(self.__max_bits):
            t1 = pick_bit(self.__state, 66) ^ pick_bit(self.__state, 93)
            t2 = pick_bit(self.__state, 162) ^ pick_bit(self.__state, 177)
            t3 = pick_bit(self.__state, 243) ^ pick_bit(self.__state, 288)
            z = t1 ^ t2 ^ t3
            yield z
            t1 = t1 ^ pick_bit(self.__state, 91) & pick_bit(self.__state, 92) ^ pick_bit(self.__state, 171)
            t2 = t2 ^ pick_bit(self.__state, 175) & pick_bit(self.__state, 176) ^ pick_bit(self.__state, 264)
            t3 = t3 ^ pick_bit(self.__state, 286) & pick_bit(self.__state, 287) ^ pick_bit(self.__state, 69)
            # Shifting and ditching last bit
            self.__state <<= 1
            self.__state = limit_mask(self.__state, 288)
            # Updating new values
            self.__state = set_bit(self.__state, 1, t3)
            self.__state = set_bit(self.__state, 94, t1)
            self.__state = set_bit(self.__state, 178, t2)

    def encode(self, plain):
        cipher_text = ""
        for c in plain:
            key_stream = self.__keystream()
            # ASCII 8bits
            x = 0
            c_int = ord(c)
            for i in range(1, 9):
                bit = next(key_stream) ^ pick_bit(c_int, i)
                x = set_bit(x, i, bit)
            cipher_text += chr(x)
        return cipher_text
