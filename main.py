import math
from stDescent import *
from nlAnalysis import *
from freqAnalysis import *

def load_crypt(fname):
    """
    Loads a cryptogram from a file
    :param fname: name of the file
    :return: just the content fo the file.
    """
    with open(fname, 'r') as file:
        data = file.read()
    return re.sub('[^A-Z]+', '', data.upper())

ciphertext = load_crypt("cryptext1.txt")
guess = get_first_guess(ciphertext)
scC = [(init_scorefct('.idea/pg2600.txt', i), math.sqrt(float(i))) for i in range(3,5)]
wcost = init_cost_spaces("words-by-frequency.txt")
dic = init_dict("words.txt")


for i in range(10):
    new_guess = find_cipher2(ciphertext, scC, initial=guess)
    sz = new_guess[2]
    szs = infer_spaces(sz, wcost[0], wcost[1])
    pns = dic_count(sz, dic, wcost)
    if pns > 0.6:
        print(pns, new_guess[1], szs)

