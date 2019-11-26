#!/bin/python
import sys

def gcd(a, b):
   if a > b:
      a, b = b, a

   fac = b // a
   remainder = b % a

   if remainder != 0:
      return gcd(a, remainder)
   else:
      return a
