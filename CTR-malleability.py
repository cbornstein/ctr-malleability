import os, sys
from binascii import hexlify

#get command line inputs
f1 = sys.argv[1]

cipher = ""
iv = ""
with open(f1, 'r') as c:
    cipher = c.read()
'''
We know the plaintext number is a multiple of 10, meaning the last digit (encoded
as a string) must end in 0, which is a decimal 48, a hex 30 or binary 0011 0000.
To "add" 5 to this integer, this string 0 must become a string 5, which is a decimal
53, hex 35, and binary 0011 0101. To accomplish this, we need to flip bits 5 and 7
XOR'ing this last digit with 0000 0101, which is a hex 0A, and a decimal 10. This
XOR must be padded as to not alter the first three digits; as such, the XOR value
is padded with a decimal 000. We therefore XOR the ciphertext with the binary string
"0b00000000000000000000000000000101" or hex 0x00000005. As a string '\0\0\0\05'
'''
mask = '\0\0\0\05'

cipherhex = hexlify(cipher)
maskhex = hexlify(mask)

newcipher = hex(int(cipherhex, 16) ^ int(maskhex, 16))

print("Original Ciphertext(hex):")
print("0x"+cipherhex)
print("New Ciphertext(hex):")
print repr(newcipher)[1:-2]

