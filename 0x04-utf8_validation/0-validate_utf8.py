#!/usr/bin/python3

"""It determines if given data set represents
a valid UTF-8 encoding"""


def validUTF8(data):
    no_bytes = 0

    mask_1 = 1 << 7
    mask_2 = 1 << 6

    for i in data:
        mask_byte = 1 << 7
        if no_bytes == 0:
            while mask_byte & i:
                no_bytes += 1
                mask_byte = mask_byte >> 1

            if no_bytes == 0:
                continue

            if no_bytes == 1 or no_bytes > 4:
                return False
        else:
            if not (i & mask_1 and not (i & mask_2)):
                return False

        no_bytes -= 1

    if no_bytes == 0:
        return True

    return False
