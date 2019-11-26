import sys

alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def encrypt(p: str, a, b):
   alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
   invalpha = { v : i for i, v in enumerate(alpha) }
   return ''.join(alpha[((a * invalpha[ch] + b) % 26)] for ch in p)

def decrypt(p: str, a, b):
   alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
   invalpha = { v : i for i, v in enumerate(alpha) }
   return ''.join(alpha[((invalpha[ch] - b) * inverse(a, 26)) % 26] for ch in p)

def inverse(a, n):
   t, newt = 0, 1
   r, newr = n, a
   while newr != 0:
      quotient = r // newr
      (t, newt) = (newt, t - quotient * newt)
      (r, newr) = (newr, r - quotient * newr)
   if r > 1: return False
   if t < 0: return t + n
   return t

def solve(v1, v2, v3, v4):
   # v1 -> v2
   # v3 -> v4
   # v1 * a + b = v2 mod 26
   # v3 * a + b = v4 mod 26
   # (v1 - v3) * a = (v2 - v4) mod 26
   # a = (v2 - v4) / (v1 - v3) mod 26
   # a * v1 + b = v2 mod 26
   # a = ((v2 - v4) % 26) / ((v1 - v3) % 26)
   # b = (v2 - (a * v1)) % 26
   coef = (v1 - v3) % 26
   invcoef = inverse(coef, 26)
   print(coef, invcoef)

   a = (v1 * invcoef) % 26
   b = (v2 - (a * v1)) % 26
   return a, b

def d2i(d, alphabet):
   a = alphabet.find(d[0])
   b = alphabet.find(d[1])
   return a * len(alphabet) + b

def i2d(i, alphabet):
   return alphabet[i // len(alphabet) % len(alphabet)] + alphabet[i % len(alphabet)]

def affine_encode_digraphs(plaintext, alphabet, a, b):
   if (len(plaintext) % 2 != 0): plaintext += 'x'
   letters = []
   for i in range(0, len(plaintext), 2):
      letters.append(i2d(a * d2i(plaintext[i:i+2], alphabet) + b, alphabet))
   return ''.join(str(l) for l in letters)

def affine_decode_digraphs(plaintext, alphabet, a, b):
   letters = []
   for i in range(0, len(plaintext), 2):
      letters.append(i2d((d2i(plaintext[i:i+2], alphabet) - b) * inverse(a, len(alphabet)**2), alphabet))
   return ''.join(str(l) for l in letters)
