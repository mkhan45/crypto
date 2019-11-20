import numpy as np
def matmul_mod(m1: np.matrix, m2: np.matrix, mod: int):
   return (m1 * m2) % mod

def inv_mat_mod(m: np.matrix, mod: int):
   det = np.linalg.det(m).round().astype(np.int)
   invdet = inverse(det, mod)
   adj = np.matrix([[m[1, 1], -m[0, 1]], [-m[1, 0], m[0, 0]]])
   return (invdet * adj) % mod

def hill_encode(mat: np.matrix, pt: str, alpha='ABCDEFGHIJKLMNOPQRSTUVWXYZ_,.'):
   if len(pt) % 2 != 0:
      pt += 'X'

   pmat = np.matrix([[alpha.find(ch) for ch in pt[::2]], [alpha.find(ch) for ch in pt[1::2]]])

   enc_mat = (mat * pmat) % len(alpha)
   enc_arr = np.array(enc_mat.T.flatten())[0]

   return ''.join([alpha[n] for n in enc_arr])

def hill_decode(mat: np.matrix, ct: str, alpha='ABCDEFGHIJKLMNOPQRSTUVWXYZ_,.'):

   mat = inv_mat_mod(mat, len(alpha))

   cmat = np.matrix([[alpha.find(ch) for ch in ct[::2]], [alpha.find(ch) for ch in ct[1::2]]])

   dec_mat = (mat * cmat) % len(alpha)
   dec_arr = np.array(dec_mat.T.flatten())[0]
   
   return ''.join([alpha[n] for n in dec_arr])

def inverse(a, n):
   if a < 0:
      a = n + a
   t, newt = 0, 1
   r, newr = n, a
   while newr != 0:
      quotient = r // newr
      (t, newt) = (newt, t - quotient * newt)
      (r, newr) = (newr, r - quotient * newr)
   if r > 1: return False
   if t < 0: return t + n
   return t
