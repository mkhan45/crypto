#!/bin/python
import sys
def isprime(n: int):
   return n % 2 != 0 and all(n % i != 0 for i in filter(lambda i: isprime(i), range(3, n // 2 + 1, 2)))

def isprime_opt(n: int, primes=[2, 3, 5]):
   for i in filter(lambda i: i in primes or isprime_opt(i, primes=primes), range(3, int(n.sqrt()) + 1, 2)):
      if i not in primes:
         primes.append(i)
      if n % i == 0:
         return False
   return True

if __name__ == "__main__":
   print(isprime_opt(int(sys.argv[1])))
