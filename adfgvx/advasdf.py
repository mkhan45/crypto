import sys
import random

def ASDFASD_encode(matrix, keyword, plaintext):
   matrix, keyword, plaintext = [''.join(list(filter(lambda ch: ch.isalnum(), s.upper()))) for s in (matrix, keyword, plaintext)]

   keyword = ''.join(set(keyword))

   if len(plaintext) % len(keyword) != 0:
      plaintext += 'Z' * (len(plaintext) % len(keyword))

   ADFGVX = { i : ch for i, ch in zip(range(6), "ADFGVX") }
   matrix_dict = { ch : ADFGVX[i // 6] + ADFGVX[i % 6] for i, ch in enumerate(matrix) }
   bigraphs = ''.join(matrix_dict[ch] for ch in plaintext)

   sorted_key = ''.join(sorted(keyword))
   keymap = {sorted_key.find(ch) : keyword.find(ch) for ch in keyword}

   columns = [ bigraphs[col : : len(keyword)] for col in range(len(keyword)) ]
   columns = [columns[keymap[i]] for i in range(len(keyword))]

   return ''.join(columns)

if len(sys.argv) == 3:
   matrix = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789")
   random.shuffle(matrix)
   matrix = ''.join(matrix)
   print("Random matrix: " + matrix)
   print(ASDFASD_encode(matrix, *sys.argv[1:]))
else:
   print(ASDFASD_encode(*sys.argv[1:]))
