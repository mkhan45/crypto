from collections import Counter

def subst_validate(alpha1, alpha2):
    """verify that alpha1 and alpha2 contain exactly the same letters, return boolean"""
    return Counter(alpha1) == Counter(alpha2)

def substitution_cipher_encode(plaintext, alpha1, alpha2):
    """prepares plaintext, validates the alphabets, and returns a ciphertext using alpha2 as the substitution cipher alphabet"""
    if Counter(alpha1) == Counter(alpha2):
       return ''.join([alpha2[alpha1.find(ch)] if ch in alpha1 else ch for ch in plaintext])
    else:
       return 'bad alphabets'

def substitution_cipher_decode(ciphertext, alpha1, alpha2):
    """prepares plaintext, validates the alphabets, and returns a plaintext using alpha1 as the original alphabet"""
    return substitution_cipher_encode(ciphertext, alpha2, alpha1)

in_str: str = input("Enter a string nerd: ").upper()
alpha1: str = input("Enter alpha 1: ").upper()
alpha2: str = input("Enter a subst alphabet: ").upper()

print(substitution_cipher_decode(in_str, alpha2, alpha1))
