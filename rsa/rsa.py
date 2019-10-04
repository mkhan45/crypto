

# This file was *autogenerated* from the file rsa.sage
from sage.all_cmdline import *   # import sage library

_sage_const_256 = Integer(256); _sage_const_0 = Integer(0)
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
   while n!= _sage_const_0 :
      v.append(chr(n % _sage_const_256 ))
      n //= _sage_const_256 
   return ''.join(v)
