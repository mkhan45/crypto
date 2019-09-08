def load_words():
    with open('words.txt') as word_file:
        valid_words = set(word_file.read().split())

    return valid_words


english_words = load_words()

inpstr = input("String:\n")

alpha = 'abcdefghijklmnopqrstuvwxyz'

for keyword in english_words:
    decode = dict()


    for i, c in enumerate(keyword):
        decode[alpha[i]] = c

    cnt = len(keyword)

    for c in filter(lambda ch: ch not in keyword, alpha):
        try:
            decode[alpha[cnt]] = c
            cnt += 1
        except:
            break


    phrase = (''.join([decode[ch] if ch in decode else ch for ch in inpstr]))

    for word in phrase.split():
        if word in english_words:
            print(keyword)
