import sys

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
