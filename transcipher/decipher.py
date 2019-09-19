in_str = "BARERTDTUTOREHJHTLUWAEUESIGIKELSOGHNSAIUFHYDISENTTOOTTTWTNWIAIHHDBSNS"
cols = 9

strlen = len(in_str)

rows = strlen//cols

num_highrows = 0
for i in range(1, cols):
   if (rows + 1) * i + (rows * (cols - i)) == strlen:
      num_highrows = i

if num_highrows == 0:
   print("Error")


out_str = ""

# out_str += in_str[:(rows + 1) * num_highrows :rows + 1]
out_str += in_str[(rows + 1) * num_highrows : : rows]

# out_str += in_str[cols : (rows + 1) * num_highrows * 2 : cols + rows + 1]

# for j in range(cols - num_highrows):
#    for i in range(num_highrows):
#       out_str += in_str[j * cols + (rows + 1) * i]

# # str2 = ""
# # # print(in_str[rows * (cols - num_highrows + 1): :rows + 1])
# # for i in range((rows + 1) * (num_highrows), strlen, rows):
# #    # print(in_str[i:i+3])
# #    str2 += in_str[i:i + (cols - num_highrows + 1)]
# str2 = ""
# for j in range(num_highrows):
#    for i in range(cols - num_highrows):
#       str2 += in_str[j * cols + num_highrows + (rows - 1) * i - 1]

# print(str2)
# for i in range(cols - num_highrows + 1):
#    print(str2[i + rows * i : i + rows*i + 3 :rows])
# for j in range(rows * (cols - num_highrows + 1), strlen , ):
#    # print(j * cols)
#    # out_str += in_str[j * : cols - num_highrows]
#    print(j)
      
      # out_str += in_str[j * cols + (rows + 1) + rows * i]
   # print(in_str[i * (rows + 1) :: rows + 1])
   # out_str += in_str[i * (rows + 1) : : rows + 1]

print(out_str)
