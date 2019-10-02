keyword = "MATH"

in_str = "VPNPMQQSLZPCTHLRHXSTLTCRIKLHIOFGUZXT"

if len(in_str) % 2 != 0: in_str += 'X'

mat = list()

for i in range(5):
   mat.append(list())
   for j in range(5):
      mat[i][j] = 0

print(mat)
