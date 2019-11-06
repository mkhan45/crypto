import sys

def ext_euclid(a, b, s=0, t=1):
   q = a // b
   r = a % b
   sn = t - q * s 
   tn = s - q * t
   if r == 0:
      return q, r, sn, tn
   else:
      return ext_euclid(q, r, s=sn, t=tn)

if __name__=='__main__':
   print(ext_euclid(int(sys.argv[1]), int(sys.argv[2])))
