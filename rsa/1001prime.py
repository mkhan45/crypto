from isprime import isprime_opt as isprime

cnt = 0
i = 0
while (cnt < 10000):
   if isprime(i):
      cnt += 1
      if(cnt % 100) == 0:
         print(cnt)
   i += 1
