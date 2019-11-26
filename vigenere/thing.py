#from subcipher import *
from math import gcd
from collections import Counter, OrderedDict

def c2i(c, alphabet):
    """Returns the index of c in the string alphabet, starting at 0"""
    # Copy your method from subcipher.py here
    return alphabet.find(c)

def i2c(i, alphabet):
    """Returns the character at index i in alphabet"""
    # Copy your method from subcipher.py here
    return alphabet[i]

def prepare_string(s, alphabet):
    """removes characters from s not in alphabet, returns new string"""
    # Copy your method from subcipher.py here
    return ''.join(list(filter(lambda ch: ch in alphabet, s)))

def vigenere_encode(plaintext, keyword, alphabet):
    """Returns plaintext encoded by vigenere cipher using key"""
    l_map = { ch : i for i, ch in enumerate(alphabet) }
    inv_alpha = { v : k for k, v in l_map.items() }
    keyword = (keyword * (len(plaintext) // len(keyword) + 1))[:len(plaintext)]
    return (''.join(inv_alpha[(l_map[ch] + l_map[keyword[i]]) % 26] for i, ch in enumerate(plaintext)))


def vigenere_decode(plaintext, keyword, alphabet):
    """Returns ciphertext decoded by vigenere cipher using key"""
    l_map = { ch : i for i, ch in enumerate(alphabet) }
    inv_alpha = { v : k for k, v in l_map.items() }
    keyword = (keyword * (len(plaintext) // len(keyword) + 1))[:len(plaintext)]
    print(''.join(inv_alpha[(l_map[ch] - l_map[keyword[i]]) % 26] for i, ch in enumerate(plaintext)))


def index_of_coincidence(ciphertext, alpha):
  """Returns index of coincidence of a certain block of ciphertext"""
  freqs = Counter(ciphertext)

  numerator = sum(freqs[alpha[i]] * (freqs[alpha[i]] - 1) for i in range(0, len(alpha)))
   
  return numerator / (len(ciphertext) * (len(ciphertext) - 1))


def friedman_test(ciphertext, alpha):
    """Calls index_of_coincidence, then returns the predicted value for keyword length from the friedman test
    using that value"""
    I = index_of_coincidence(ciphertext, alpha)
    return 0.027 * len(ciphertext) / \
    (0.0655-I+len(ciphertext)*(I-0.0385))


def kasiski_test(ciphertext):  #Code partially provided
    """Finds gcd of most common distances between repeated trigraphs
    Recommended strategy: loop through the ciphertext, keeping a list of trigraphs and a list of distances in this way:
    1) When encountering a new trigraph add it to the trigraph list
    2) When encountering a repeat add the distance from current index to first index of that trigraph to the list of distances"""
    # Here, write code to create the array of distances:

    # Code is provided to find the gcd of any common distances appearing at least twice, just add your array:

    trigraphs = [ciphertext[i:i+3:] for i in range(len(ciphertext) - 2)]

    dists = []
    repeated_tris = []

    for trigraph in trigraphs:
      fi = ciphertext.find(trigraph)
      si = ciphertext.find(trigraph, fi + 3)
      if si != -1 and trigraph not in repeated_tris:
        dists.append(si - fi)
        repeated_tris.append(trigraph)
    
    dCount = Counter(dists)
    topCount = dCount.most_common(6)
    my_gcd = topCount[0][0]
    for index in range(1, len(topCount)):
        if topCount[index][1] > 1:
            my_gcd = gcd(my_gcd, topCount[index][0])
    return my_gcd

def run_key_tests(ciphertext, alphabet): #Code provided
    """Runs Friedman and Kasiski tests and formats the output nicely"""
    friedman = friedman_test(ciphertext, alphabet)
    kasiski = kasiski_test(ciphertext)
    out = "Friedman test gives: " + str(friedman) + " and Kasiski gives this as the most likely: " + str(kasiski);
    return out

def make_cosets(text, n):
    """Makes cosets out of a ciphertext given a key length; should return an array of strings"""
    return [text[i: : n] for i in range(n)]

def rotate_list(old_list):  #Code provided
    """Takes the given list, removes the first element, and appends it to the end of the list, then returns the
    new list"""
    if type(old_list) == str:
      old_list = list(old_list)
    new_list = old_list[:]
    new_list.append(old_list[0])
    del new_list[0]
    return new_list

def rotate_list_n(ls, n):
  nls = ls[:]
  for i in range(n):
    nls = rotate_list(nls)
  return nls

def find_total_difference(list1, list2):
    """Takes two lists of equal length containing numbers, finds the difference between each pair of matching
    numbers, sums those differences, and returns that sum"""
    return sum(abs(a - b) for a, b in zip(list1, list2))

def find_likely_letters(coset, alpha, eng_freq):
    """Finds the most likely shifts for each coset and prints them
    Recommended strategy: make a list of the frequencies of each letter in the coset, in order, A to Z.
    Then, alternate using the find total difference method (on your frequencies list and the standard english
    frequencies list) and the rotate list method to fill out a new list of differences.  This makes a list of
    the total difference for each possible encryption letter, A to Z, in order.
    Then, find the indices of the smallest values in the new list, and i2c them for the most likely letters."""

    #return statement provided.  feel free to replace "letter1" and "letter2" with other variable names.
    cstr = prepare_string(coset, alpha)
    counter = Counter(cstr)   
    freqs = [ counter[ch] / len(cstr) for ch in alpha ]
    d = {}
    for i in range(26):
      d[alpha[i]] = find_total_difference(freqs, eng_freq)
      freqs = rotate_list(freqs)
      #print(cstr)

    #print(d)
    d = sorted(d, key=lambda i: d[i])
    return f"the most likely letter is: {d[0]} followed by: {d[1]}"

def crack(ciphertext, alpha, eng_freq):  #Code provided
    """User-friendly walkthrough of decoding methods"""
    print("Your cipher text is: " + ciphertext)
    out = run_key_tests(ciphertext, alpha)
    print(out)
    x = int(input("Choose the key length you'd like to try: "))
    cosets = make_cosets(ciphertext, x)
    for index in range(len(cosets)):
        print("For coset " + str(index + 1) + ", " + find_likely_letters(cosets[index], alpha, eng_freq) + ".")
    s = input("Type the key you would like to use to decipher: ")
    print(vigenere_decode(ciphertext, s, alpha))
    print()




#alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

#eng_freq = [.0817, .0149, .0278, .0425, .1270, .0223, .0202, .0609, .0697, .0015, .0077, .0403, .0241, .0675, .0751,
#            .0193, .0010, .0599, .0633, .0906, .0276, .0098, .0236, .0015, .0197, .0007]

#example = "UZRZEGNJENVLISEXRHLYPYEGTESBJHJCSBPTGDYFXXBHEEIFTCCHVRKPNHWXPCTUQTGDJHTBIPRFEMJCNHVTCFSAIIJENREGSALHXHWZWRZXGTTVWGDHTEYXISAGQTCJPRSIAPTUMGZALHXHHSOHPWCZLBRZTCBRGHCDIQIKTOAAEFTOPYEGTENRAIALNRXLPCEPYKGPNGPRQPIAKWXDCBZXGPDNRWXEIFZXGJLVOXAJTUEMBLNLQHGPWVPEQPIAXATYENVYJEUEI"
## For the example, the key is "PLANET" and the plaintext is:
## "For many years the known planets of our solar system were mercury, venus, earth, mars, jupiter, saturn, uranus, neputne, and pluto.  However, it is now true that many people think pluto should no longer be considered a named planet.  New planets are currently being discovered, and it is very likely that many more will be in the near future."

##Try this:
##crack(example, alpha, eng_freq)

##Once everything works, uncomment the following twelve lines and crack some ciphertexts!
#c1 = "KBTCSPDTIPHTVITZTTKGAMCGWGOWUWQDTZXRGGIMUADETJWHGHCGIYROHRPYGNATSPZDULMOISIQEAEFEFKXRWSAQHWBSPTDVTNMATKTSHKEROGCPLDGUMSHYCDOXARCCQUOJMHGUGCPTKIAOKPPXFQHUEOCADNLTIPHWCPMGNNVCUQEAEBHCJTWDUOBLNPTEGAFMEFKXRWSHXCKOANDWWKSPCIMCLQMHCHQSIYGNWKZAFPVWTLCUVWPSLKUEYAYETGIYQIZLDWZHWNIRINYGNATSBWAAHMORFJLHALLIZVJLSRWWSKLIWUPKTNFWILTVWKLCUHMGIKLLQKNMJLMVKAGDLDFSZUPMDSLIDEPCMIFTPJBCGPNKTGAOIPUNMJADBNMKWGRHKAANZRMCTSBNCRDUCLGTDYVXAWWAELYWECPLDROWFBCBOJROHTIFTFSVEQTIFXSMGIXSGQTAFWOXSGUGILXIVKXRWMQHWPGDDIWSKEOSBCHOXMLQQZCGTOHPQWCRDHGAOJCWMWOZIOKBIMW"
#c2 = "ZSIEVVOZGHYEEFCBQDRSGDGAMFNIGKIDZCEELDBPQIIHNQUUFUFUGZSZLVVPURBQJWXNFXOZKSIIGQHTWJZOPHWEOIKRHGCUFUNIGPMPSIXHGHFGLSCLHUUUJZESUHGMQAPDNGWEVSUTUHBIZCNAFSVAFSYEEHWESBFTUHFOGDPPNVHMZOJAABCZWFVAYOMNWSEFNUSHWBRSQHQUVSUTBXGQWJVNTRKMFHKOQRZAGYDOEHZUCSYIRYSDQCEEVPBQOAPNNPSUKYRTLEIFMQRNPDZXESKEUSSZYIZNBIRAGACOYDGGUOESRHWYNSIYEDBPGAKHNWGIZMZCNPSTWFVTBRAQWHIAAGCYHDCLVNSYWWCIXHHAOOKCULBHSRVRFLAULGDYSDJAJWKEGYGTGKSCHCWFKGFOBRFMFRFMAHKMQGZHBSSFGARKRDZALCWFEHWZVGYEEHGAYWMEZHZALGFFPRAYWBKSRVRAGCFOBPAYEADMRESUFFRNQRAMYOZNUHVQLCFDYHG"
#c3 = "PHXWBQDQAHGKSNVHZZYOEHISPVLELEJRDSICZAEPKJHKTKFMLVJPOWPWTCNASTQABESKLLLDQTRSLOPTAXETPCSSWCAAGHJLPTAUONAZDSPPREMSXGVVIDEKINASTQAGASJLZQCPHXHRJRICZVHMTWZQCPHXEZJKQHCULXZFNXGKPAITALARKMBRXLYCTEWHYCVUBLKNWIISULPXSXRKXHKTOPKIJWUBDJEOIIQZQSAALXYWTICOABHRFKAIELECFMDQAHHTZVLVODKNMLVDHAIXRBHXWDQAHFTPCTLPXJDRSLSULIDEEEJLSQVDTLAZDSODKUMJFDSWLADUCKZLAJJTAIDGVVPJDMLVKAIGOAGHJLPTAUONAZDSPPREMSXGVVNKUPMCDJWBATHVVYPWCOMHVVVLADHAMIRFKEGATVLVVAPPJYHYVNLZSNETQVVJWJHDXBZKAXAWCXWFXZWGNOPGIWHBTZEGXZJLTNXYMLRLTMPJSNTVJZBXPIHRNZPKWUONCFMYATHFAEMWWCIWBHYKXVZHKLHRXTBBHPIEPPGBEXHLAEMWAWVKOG"
#c4="YRDOIQCGDEJEHWWYUSTOGSPZYEETMWSGDOWEMVSIENRPYDRUNEXSBLQKAKVEJKMJMBEOLPECXYCALJIEASVOOWSWATYELSIFBLVSVXWZZEJSGUTIANXSUJVVQSNINKQIYOFNSDRUIOLLXOMBQTFAXGXYMTGRIIIJEOISHDTVUSRNOJPPSIKMLSEUROFTQRYCPLZKYWSIQGZSNHVYUSRSNRRZEHDEHWXYMTRNCGMFFLZKYWLRFEMELEITMMVAJUSWQSJOLPVNARDTULPSUDJPLRJVESFRMQEGQGFOXGEPMNUAXYMJQSYIGWSNMSYHCVLRURKHYVPZYESAFO"
#c5="VBLTRYTHHHIPEXTGJSZMGEDSTASZMAAZLGCIEGKKDSVWLVTSLNHJFYCBMEKFQDLNAGHMKKZXRLSYMSOLPLBLXBGPMIFAMHMGHPXFWVBFAPHXBZEGCSUWIPQILNXKUZBTYGSSTFEALYGBGPZGVWYLZMVVFVWKKZHJFEALQHQWQCIEBLTSLJLQBZEENJKTQBZEEOMTWSFMMGDNGYCCPMENKQWLLPELBGPZXVBYMDVVOIGZYXUAVHPTMVFNMVVJJPMVGLJLIABMKDHNHRGPELZDYHCFOVHVFKUHRMHMNMPKIEAXTMVJVAGPITAKVYYFMWMLWVHTUGWBBSNHWFMVMHGPZSSITAHDQZSCPIKGSXLFRMRTQJKCIQIXBSAUHPJICLVWNSEALABRWVVJVZWMZKMVRRAIEEOJHXZWVTKAVFHBBLXXGTKSRALXZAOHX"
#c6= "SIKSZDISXFCFGABPJGVDYJPRKRNPCEZMGJIZVCHHOFMMLUQQAOELRGJIZHGRAVIWILDHVYQEDWTJXULCMQKHOXCJRPQBOCOFQYOHGTBWREEUOLVSMIRMBWAJRZIGKRFZCFEGEMPWVNFEESSPGUXBRBWAIMOXFSYKKIXMTLQYSLYZBKKPXKMNPKFPLCJKXTPGYRKZFFCSACABOCBRFIWIPMEWPFMFOQASVFPSNMMUMRGGJISMQYGJEUMKHNMMOKGOVPXOITSEISORYGUWXZSSCHVIWIPMJJISIGAYQSLMLUAQAJQQIETSVRBSQDCZSSFROFSEASOCFZMAOAUIFCMIEJEMSWCHMRPAWCHTINCQOIKRHKPOPGCPYPSRXISCRVVPKJRCSQCREQMFRKXTAPWGVIOEJZBXISCMIEHEDIZOOAMDELTRGPZSSFUCPPTPOLKXXSLHSCHFEUOLKGBRDSRNCPYPVNNSIEJCUCPPMAOAUIFCMIEJEMSFOYQLBPMWPCRGICZLQYSLYZBJEMSFOYQMDELGRGCPYPVNNSIEJCUCPP"
#crack(c1, alpha, eng_freq)
#crack(c2, alpha, eng_freq)
#crack(c3, alpha, eng_freq)
#crack(c4, alpha, eng_freq)
#crack(c5, alpha, eng_freq)
#crack(c6, alpha, eng_freq)

