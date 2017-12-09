from string import ascii_uppercase as alph
import operator

"""
The following are the hard coded relative frequencies of the single letters
in the English alphabet. This code can be generalized to any given linguistic
corpus.
"""

englishLetterFreq = \
    {'E': 12.70, 'T': 9.06, 'A': 8.17, 'O': 7.51, 'I': 6.97, 'N': 6.75, 'S': 6.33, 'H': 6.09, 'R': 5.99, 'D': 4.25, 'L': 4.03, 'C': 2.78, 'U': 2.76, 'M': 2.41, 'W': 2.36, 'F': 2.23, 'G': 2.02, 'Y': 1.97, 'P': 1.93, 'B': 1.29, 'V': 0.98, 'K': 0.77, 'J': 0.15, 'X': 0.15, 'Q': 0.10, 'Z': 0.07}
etaoin = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'

def shift(plaintext, key, alphabet):
    """
    This function encodes (decodes) plaintext using key as a key,
    which is just a permutation of alphabet.
    :param plaintext: text to encode/decode.
    :param key: the permutation key.
    :param alphabet: the alphabet to use a reference for key.
    :return: the encoded (decoded) text.
    """
    keyIndices = [alphabet.index(k.upper()) for k in plaintext]
    return ''.join(key[keyIndex] for keyIndex in keyIndices)

def get_count(s):
    """
    Just return the length of s
    :param s: a string.
    :return: len(s).
    """
    return len(s)

def get_letter_count(s):
    """
    This function returns a dictionary that encodes
    the frequency distribution of the characters in s.
    :param s: input string.
    :return: frequency dictionary.
    """
    tot_count = get_count(s)
    let_count = {'A' : 0}
    for l in alph:
        let_count[l] = 0
    for e in s.upper():
        if e in let_count.keys():
            let_count[e] += 100 / tot_count
        else:
            let_count[e] = 100 / tot_count
    return let_count

def get_freq_string(s):
    """
    Given a message, this function analyses its frequencies
    and returns a copy of the English alphabet ordered
    according to these frequencies.
    :param s: the message to analyse.
    :return: the ordered alphabet.
    """
    letter_count = get_letter_count(s)
    sorted_dict = sorted(letter_count.items(), key=operator.itemgetter(1))
    sorted_dict.reverse()
    return sorted_dict

def get_first_guess(s):
    """
    Gives a first well-educated guess for key decoding s.
    :param s: the string to decode.
    :return:
    """
    freq_string = get_freq_string(s)
    sz = ''.join([e[0] for e in freq_string]).upper()
    return shift(alph, sz, etaoin)
