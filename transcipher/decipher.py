import sys

# in_str = "BARERTDTUTOREHJHTLUWAEUESIGIKELSOGHNSAIUFHYDISENTTOOTTTWTNWIAIHHDBSNS"
# in_str = "IHOSTSMTEFIHTEWBTTEOSAEIWWFSSMAOTTTESRI"
in_str = ''.join(filter(lambda ch: ch != ' ', sys.argv[1])).upper()
print(in_str)
# cols = int(sys.argv[2])
min_cols, max_cols = [int(n) for n in sys.argv[2:4]]
if len(sys.argv) == 5:
   keyword = sys.argv[4].upper()
else:
   keyword = ''

strlen = len(in_str)
print(strlen)

for cols in range(min_cols, max_cols):
   rows = strlen//cols

   num_highrows = 0
   for i in range(1, cols):
      if (rows + 1) * i + (rows * (cols - i)) == len(in_str):
         num_highrows = i

   # print('\n'.join([in_str[i : (rows + 1) * num_highrows : rows + 1] + in_str[(rows + 1) * num_highrows + i: : rows] for i in range(rows + 1)])[:-(cols - num_highrows - 1)] + "\n")

   sorted_key = ''.join(sorted(keyword))

   map = {keyword.find(ch) : sorted_key.find(ch) for ch in keyword}
   # print(map)
   # print(map.values())

   table = [in_str[i : (rows + 1) * num_highrows : rows + 1] + in_str[(rows + 1) * num_highrows + i: : rows] for i in range(rows + 1)]

   print('\n'.join(table))

   if len(keyword) != 0:
      print(sorted_key + "\n")
      outstr = '\n'
      for row in table:
         # map is sorted
         try:
            outstr += ''.join([row[i] for i in map.values()]) + "\n"
         except:
            pass

      print(outstr + "\n")

# for i in range(rows + 1):
#    out_str += in_str[i : (rows + 1) * num_highrows : rows + 1]
#    out_str += in_str[(rows + 1) * num_highrows + i: : rows]

