import numpy as np
import itertools as it

def matmul_mod(m1: np.matrix, m2: np.matrix, mod: int):
   return (m1 * m2) % mod

def inv_mat_mod(m: np.matrix, mod: int):
   det = np.linalg.det(m).round().astype(np.int) % mod
   if det < 0:
      return None
   invdet = inverse(det, mod)
   adj = np.matrix([[m[1, 1], -m[0, 1]], [-m[1, 0], m[0, 0]]])
   return (invdet * adj) % mod

def hill_encode(mat: np.matrix, pt: str, alpha='ABCDEFGHIJKLMNOPQRSTUVWXYZ_,.'):
   # pt = pt.upper().replace(' ', '')
   if len(pt) % 2 != 0:
      pt += 'X'

   pmat = np.matrix([[alpha.find(ch) for ch in pt[::2]], [alpha.find(ch) for ch in pt[1::2]]])

   enc_mat = (mat * pmat) % len(alpha)
   enc_arr = np.array(enc_mat.T.flatten())[0]

   return ''.join([alpha[n] for n in enc_arr])

def hill_decode(mat: np.matrix, ct: str, alpha='ABCDEFGHIJKLMNOPQRSTUVWXYZ_,.'):
   return hill_encode(inv_mat_mod(mat, len(alpha)), ct, alpha)


def inverse(a, n):
   for i in range(n):
      if (i * a) % n == 1:
         return i
   return None


# def inverse(a, n):
#    if a < 0:
#       a = n + a
#    t, newt = 0, 1
#    r, newr = n, a
#    while newr != 0:
#       quotient = r // newr
#       (t, newt) = (newt, t - quotient * newt)
#       (r, newr) = (newr, r - quotient * newr)
#    if r > 1: return False
#    if t < 0: return t + n
#    return t

def try_digraphs(alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
   digraphs = it.permutations(alpha, 2)
   mat = np.matrix([[7, 6], [4, 13]])
   for a, b in digraphs:
      if hill_encode(mat, a + b, alpha=alpha) == a + b:
         print(a + b)

def gcd(a, b):
   if a > b:
      a, b = b, a

   fac = b // a
   remainder = b % a

   if remainder != 0:
      return gcd(a, remainder)
   else:
      return a

def find_key(d1, d2, crib1, crib2, alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
   tmatrix = np.matrix([[alpha.find(ch) for ch in d1], [alpha.find(ch) for ch in d2]])
   cribmatrix = np.matrix([[alpha.find(ch) for ch in crib1], [alpha.find(ch) for ch in crib2]])

   invcrib = inv_mat_mod(cribmatrix, len(alpha))

   key = matmul_mod(invcrib, tmatrix, len(alpha))
   return key.T

def find_key_ext(t, crib, alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"): 
   tdigs = [t[i:i+2] for i in range(len(t) - 1)]
   cdigs = [crib[i:i+2] for i in range(len(crib) - 1)]

   for a, c in zip(tdigs, cdigs):
      for b, d in zip(tdigs, cdigs):
         try:
            key = find_key(a, b, c, d, alpha)
            print(a, b, c, d, key, hill_encode(key, crib, alpha))
            if hill_encode(key, crib, alpha) == t[:len(crib)]:
               print("!!!!!!")
               return key
         except:
            pass
