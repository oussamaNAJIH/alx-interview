#!/usr/bin/python3
"""
You can use the following approach to implement the validUTF8 function:

Iterate through each byte in the data set.
Check if the byte represents a single-byte character (starts with '0'),
if so, move to the next byte.
If the byte represents a multi-byte character, determine the number of
bytes in the character by counting the consecutive leading '1' bits
until a '0' bit is encountered. This will indicate the number of bytes
in the character.
If the number of bytes is not within the range of 1 to 4, return False.
Check if the following bytes (if any) start with '10' bits, indicating
continuation bytes. If not, return False.
Continue this process until you have iterated through all bytes
in the data set.
If all bytes are valid according to the UTF-8 encoding rules, return True.
"""


def check_bytes(num):
    """
    Returns how many bytes needed to represent num in UTF-8 encoding
    """
    base = 1 << 7
    count = 0
    while base & num:
        count += 1
        base >>= 1
    return count


def validUTF8(data):
    """
    determines if a given data set represents a valid UTF-8 encoding
    """
    count = 0
    for item in data:
        if count == 0:
            count = check_bytes(item)
            if count == 0:
                continue
            if count == 1 or count > 4:
                return False
            count -= 1
        else:
            if check_bytes(item) != 1:
                return False
            count -= 1
    if count == 0:
        return True
    return False
