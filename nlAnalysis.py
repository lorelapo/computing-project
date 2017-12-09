# import nltk
# import re

# sentence =  """At eight o'clock on Thursday morning... Arthur didn't feel very good."""
# tokens = nltk.word_tokenize(sentence)
# print(tokens)
# tagged = nltk.pos_tag(tokens)
# print(tagged[0:6])

from math import log

def init_cost_spaces(fname):
    """
    Builds a cost dictionary, assuming Zipf's law and cost = -math.log(probability).
    :param fname: the file containg the dictionary
    :return: the dictionary with, for each word, a cost given by Zipf's law, together
             with the word of maximal length
    """
    with open(fname) as file:
        words = file.read().upper().split()

    wordcost = dict((k, log((i+1)*log(len(words)))) for i,k in enumerate(words))
    maxword = max(len(x) for x in words)

    return (wordcost, maxword)

def infer_spaces(s, wordcost, maxword):
    """
    Uses dynamic programming to infer the location of spaces in a string s
    without spaces.
    Code from:
    https://stackoverflow.com/questions/8870261/how-to-split-text-without-spaces-into-list-of-words
    :param s: the string to analyse.
    :param wordcost: the vector containing the cost of each word
    :param maxword: the length of the longest word in our dictionary
    :return: the best match.
    """

    # Find the best match for the i first characters, assuming cost has
    # been built for the i-1 first characters.
    # Returns a pair (match_cost, match_length).
    def best_match(i):
        candidates = enumerate(reversed(cost[max(0, i-maxword):i]))
        return min((c + wordcost.get(s[i-k-1:i], 9e999), k+1) for k,c in candidates)

    # Build the cost array.
    cost = [0]
    for i in range(1,len(s)+1):
        c,k = best_match(i)
        cost.append(c)

    # Backtrack to recover the minimal-cost string.
    out = []
    i = len(s)
    while i>0:
        c,k = best_match(i)
        assert c == cost[i]
        out.append(s[i-k:i])
        i -= k

    return " ".join(reversed(out))

def init_dict(fname):
    """
    Initialize the dictionary for the language analysis.
    :param fname: name of the file containing the dictionary.
    :return: list of words (i.e. the actual dictionary).
    """
    with open(fname) as file:
        dictionary = file.read().upper().split()
    return dictionary

def dic_count(s, dic, wcost):
    """
    Given a string s infers the number of spaces in this string
    and, using the dictionary dic, finds the fraction of words
    in s that are in the given dictionary.
    :param s: string to analyse.
    :param dic: dictionary to use for the analysis.
    :param wcost: argument for infer_spaces
    :return: fraction of words of s that are in dic.
    """
    count = 0

    ssep = infer_spaces(s.upper(), wcost[0], wcost[1])
    l = ssep.split()

    totalcount = len(l)

    for word in l:
        if word in dic:
            count +=1

    return count/totalcount

# print(dicCount(s, dictionary))