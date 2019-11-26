from gcd import gcd
for i in range(20, 60):
   a_poss = sum(gcd(j, i) == 1 for j in range(1, i))
   b_poss = i
   print(f"{i}\t {a_poss} \t {b_poss} \t {a_poss * (b_poss) - 1}")
