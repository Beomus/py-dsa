"""
Caesar Cipher Encryptor

Given a non-empty string of lowercase letters and a non-negative integers
representing a key, write a function that returns a new string obtained by shifting
every letter in the input string by k postiion in the alphabet where k is the key.
"""


def caesarCipher(string: str, key: int) -> str:
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    encoded = []
    for char in string:
        if char in alphabet:
            curIndex = alphabet.index(char)
            shiftedIndex = (curIndex + key) % len(alphabet)
            encoded.append(alphabet[shiftedIndex])
        else:
            encoded.append(char)
    return "".join(encoded)


def caesarCipherEncryptor(string, key):
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    return "".join([alphabet[(alphabet.index(char) + key) % 26] for char in string])
