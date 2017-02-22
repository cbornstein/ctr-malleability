# ctr-malleability
Python program that illustrates the malleability of block cipher encryption used in counter or CTR mode.

# Explanation:
This program demonstrates a potential vulnerability in the use of CTR mode when implementing block cipher encryption. The means by which CTR mode is implemented allows a bit flipped in the ciphertext to also be flipped in the plaintext. Decryption of this modified ciphertext will still take place, but the plaintext is now changed. This is potentially adventageous for an adversary.

A useful explanation of this topic can be found here: 
http://crypto.stackexchange.com/questions/33846/is-regular-ctr-mode-vulnerable-to-any-attacks

This program illustrates this weakness by modifiying a given ciphertext. The example ciphertext, which we know to be an ascii string of which the first four characters are the ascii character representation of a four digit number divisible by ten. We can "add" 5 to this number by calculating a bit mask that will change the last digit of this number from a zero to a five. This property is known as mallebility.

The sample ciphertext is taken as a command line argument. This is obviously a specific example and is meant for illustrative purposes only.
