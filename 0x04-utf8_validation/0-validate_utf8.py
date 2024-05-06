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


# def check_bytes(num):
#     """
#     Returns how many bytes needed to represent num
#     """
#     ref = 1 << 7
#     count = 0
#     while num & ref:
#         ref >>= 1
#         count += 1
#     return count
def validUTF8(data):
    num_bytes = 0
    for byte in data:
        byte_bin = bin(byte)[2:].zfill(8)
        if num_bytes == 0:
            if byte_bin[0] == '0':
                continue
            elif byte_bin[:3] == '110':
                num_bytes = 2
            elif byte_bin[:4] == '1110':
                num_bytes = 3
            elif byte_bin[:5] == '11110':
                num_bytes = 4
            else:
                return False
            num_bytes -= 1
        else:
            if not byte_bin.startswith('10'):
                return False
            num_bytes -= 1
    return num_bytes == 0
