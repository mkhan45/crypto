import sage.crypto
import sage.crypto.util

def decode(c, n, e):
   totient = sage.crypto.util.carmichael_lambda(n)
   d = e.inverse_mod(totient)
   m = power_mod(c, d, n)
   return m, d

def ascii_decode(n):
   n = Integer(n)
   v = []
   while n!= 0:
      v.append(chr(n % 256))
      n //= 256
   return ''.join(v)
