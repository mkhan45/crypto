def prepare_string(s, alphabet):
    """removes characters from s not in alphabet, returns new string"""
    return ''.join(list(filter(lambda ch: ch in alphabet), s))

def caesar_shift_encode(plaintext, shift, alphabet):
    """prepares plaintext and returns a new string shifted by shift, relative to alphabet"""
    map = {ch : alphabet[(i + shift) % len(alphabet)] for i, ch in enumerate(alphabet)}
    return ''.join([map[in_ch] if in_ch in alphabet else in_ch for in_ch in plaintext])

def caesar_shift_decode(ciphertext, shift, alphabet):
    """return the plaintext, shifted by shift, relative to alphabet"""
    return caesar_shift_encode(ciphertext, -shift, alphabet)

def load_words():
    with open('words.txt') as word_file:
        valid_words = set(word_file.read().split())

    return valid_words

in_str = input("Enter a string: ").split()

words = load_words()

alphabet = 'abcdefghijklmnopqrstuvwxyz'.upper()

for shift in range(1, 26):
   # if all([caesar_shift_encode(word, shift, alphabet) in words for word in in_str]):
   #    print(shift, caesar_shift_encode(' '.join(in_str), shift, alphabet))
   print(shift, caesar_shift_encode(' '.join(in_str), shift, alphabet))
