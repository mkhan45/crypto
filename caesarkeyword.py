inpstr = input("String:\n")
keyword = input("Keyword:\n")

en = True if input("Encode? (Y or N):\n") == 'Y' else False

decode = dict()

alpha = 'abcdefghijklmnopqrstuvwxyz'

for i, c in enumerate(keyword):
    decode[alpha[i]] = c

cnt = len(keyword)

for c in filter(lambda ch: ch not in keyword, alpha):
    decode[alpha[cnt]] = c
    cnt += 1


if not en:
    encode = {v : k for k, v in decode.items()}
    # print(encode)
    print(''.join([encode[ch] if ch in encode else ch for ch in inpstr]))
else:
    print(''.join([decode[ch] if ch in decode else ch for ch in inpstr]))
