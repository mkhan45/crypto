from PIL import Image
import numpy as np

def hill_encode(mat: np.matrix, pt):
   shape = pt.shape
   pt = pt.flatten()
   pmat = np.matrix([pt[::2], pt[1::2]])

   enc_mat = (mat * pmat) % 256
   enc_arr = np.array(enc_mat.T.flatten())[0]

   return enc_arr.reshape(shape).astype(np.uint8)

def hill_decode(mat: np.matrix, ct):
   return hill_encode(inv_mat_mod(mat, 256), ct)

def inv_mat_mod(m: np.matrix, mod: int):
   det = np.linalg.det(np.matrix(m)).round().astype(np.int) % 256
   if det < 0:
      return None
   invdet = inverse(det, mod)
   adj = np.matrix([[m[1, 1], -m[0, 1]], # [d, -b]
                   [-m[1, 0], m[0, 0]]]) # [-c, a]
   return (invdet * adj) % mod

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

im = Image.open("Disco.bmp").convert("L")
size = im.size

im = np.array(im)

im2 = im + 53 % 256


im2 = Image.fromarray(im2)

im2.save("im2.png")


im = np.array(Image.open("SC.bmp").convert("L"))
im3 = hill_encode(np.matrix([[2, 5], [3, 20]]), im)
im3 = Image.fromarray(im3)
im3.save("im3.png")

im = np.array(Image.open("Mystery1.bmp").convert("L"))
im4 = hill_decode(np.matrix([[2, 5], [3, 20]]).T, im)
im4 = Image.fromarray(im4)
im4.save("im4.png")

def superhill_enc(mat: np.matrix, pt: np.matrix, vector: np.array):
   shape = pt.shape
   pt = pt.flatten()

   vector = np.array(vector)

   pmat = pt.reshape((-1, 2))

   for i in range(pmat.shape[0]):
      pmat[i] = hill_encode(mat, pmat[i])
      # pmat[i] = (pmat[i] * mat) % 256
      if i % 2 == 0:
         # print(mat[0, 0], mat[0, 0] * vector[0], vector[0])
         mat[0, 0] = mat[0, 0] * vector[0, 0] % 256
         mat[0, 1] = mat[0, 1] * vector[0, 1] % 256
      else:
         mat[1, 0] = mat[1, 0] * vector[0, 0] % 256
         mat[1, 1] = mat[1, 1] * vector[0, 1] % 256
   return pmat.reshape(shape)

def superhill_dec(mat: np.matrix, pt: np.matrix, vector: np.array):
   shape = pt.shape
   pt = pt.flatten()

   # vector = np.array(vector)

   pmat = pt.reshape((-1, 2))

   for i in range(pmat.shape[0]):
      # print(mat, inv_mat_mod(mat, 256))
      pmat[i] = hill_decode(mat, pmat[i])
      # print(vector, pmat[i])
      # pmat[i] = (pmat[i] * mat) % 256
      if i % 2 == 0:
         mat[0, 0] = mat[0, 0] * vector[0] % 256
         mat[0, 1] = mat[0, 1] * vector[1] % 256
      else:
         mat[1, 0] = mat[1, 0] * vector[0] % 256
         mat[1, 1] = mat[1, 1] * vector[1] % 256
   return pmat.reshape(shape)

# im = np.array(Image.open("SC.bmp").convert("L"))
# im5 = superhill_enc(np.matrix([[2, 5], [3, 20]]), im, np.matrix([5, 9]))
# im5 = Image.fromarray(im5.astype(np.uint8))
# im5.save("im5.png")

# im = np.array(Image.open("Mystery2.bmp").convert("L"))
# im6 = superhill_dec(np.matrix([[2, 5], [3, 20]]), im, np.array([101, 141]))
# im6 = Image.fromarray(im6.astype(np.uint8))
# im6.save("im6.png")

# im = np.array(Image.open("Mystery3.bmp").convert("L"))
# im7 = superhill_dec(np.matrix([[2, 5], [3, 20]]), im, np.array([5, 9]))
# im7 = Image.fromarray(im7.astype(np.uint8))
# im7.save("im7.png")

# im = np.array(Image.open("Mystery3.bmp").convert("L"))
# im7 = superhill_dec(np.matrix([[2, 5], [3, 20]]), im, np.array([5, 9]))
# im7 = Image.fromarray(im7.astype(np.uint8))
# im7.save("im7.png")

# im = np.array(Image.open("logo1.bmp").convert("L"))
# im8 = superhill_enc(np.matrix([[2, 5], [3, 20]]), im, np.matrix([5, 9]))
# im8 = Image.fromarray(im8.astype(np.uint8))
# im8.save("im8.png")

# im = np.array(Image.open("logo2.bmp").convert("L"))
# im9 = superhill_enc(np.matrix([[2, 5], [3, 20]]), im, np.matrix([5, 9]))
# im9 = Image.fromarray(im9.astype(np.uint8))
# im9.save("im9.png")
