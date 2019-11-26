#!/bin/python
import sys
from numba import njit, jit
from numba import uint64
import numpy as np
def isprime(n: int):
   return n % 2 != 0 and all(n % i != 0 for i in filter(lambda i: isprime(i), range(3, n // 2 + 1, 2)))

@njit
def isprime_2(n: np.int) -> bool:
   if n % 2 == 0:
      return False

   for i in range(3, int(float(n)**0.5), 2):
      if n % i == 0:
         return False

   return True


if __name__ == "__main__":
   print(isprime_2(np.int(sys.argv[1])))
