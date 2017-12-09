from heapq import nlargest
from itertools import combinations
from random import choice, shuffle
from string import ascii_uppercase as LETTERS
import re
from collections import Counter
from math import log

def ngram_count(n, text):
    """Return the number of n-grams in text."""
    return len(text) - n + 1

def ngrams(n, text):
    """Generate the n-grams in text.

    >>> list(ngrams(3, 'HELLOWORLD'))
    ['HEL', 'ELL', 'LLO', 'LOW', 'OWO', 'WOR', 'ORL', 'RLD']

    """
    for i in range(ngram_count(n, text)):
        yield text[i:i+n]

def plaintext_score_function(n, corpus):
    """Return a function that scores a plaintext based on the
    log-likelihood of the occurrence of n-grams compared to those
    found in corpus.

    """
    # Number of n-grams in the corpus
    k = ngram_count(n, corpus)

    # Count of occurrences of each n-gram in the corpus.
    counts = Counter(ngrams(n, corpus))

    # Map from n-gram to the logarithm of its frequency in the corpus.
    log_freq = {ngram: log(count / k) for ngram, count in counts.items()}

    # Log-frequency to use for n-grams that don't appear in the corpus
    # (an arbitrary value that's much smaller than the log-frequency
    # for any n-gram that does appear in the corpus).
    min_log_freq = log(0.01 / k)

    def score(plaintext):
        return sum(log_freq.get(ngram, min_log_freq)
                   for ngram in ngrams(n, plaintext))
    return score


def init_scorefct(fname, n):
    """ Generate a scoring function analyzing the n-grams from the corpus
    contained in the file fname"""

    with open(fname, encoding="utf-8") as f:
        text = f.read()

    # corpi = [re.sub('[^A-Z]+', '', text1.upper()), re.sub('[^A-Z]+', '', text2.upper()), re.sub('[^A-Z]+', '', text3.upper())]
    corpus = re.sub('[^A-Z]+', '', text.upper())
    return plaintext_score_function(n, corpus)


def decipher(ciphertext, cipher):
    """Decipher ciphertext according to cipher, which must be an iterable
    giving a permutation of uppercase letters.

    >>> decipher('URYYBJBEYQ', 'NOPQRSTUVWXYZABCDEFGHIJKLM') # rot-13
    'HELLOWORLD'

    """
    return ciphertext.translate(str.maketrans(''.join(cipher), LETTERS))

def find_cipher(ciphertext, score_fun, initial=None, choices=10):
    """Attempt to decrypt ciphertext, using score_fun to score the
    candidate plaintexts. Return a tuple (score, cipher, plaintext)
    for the best cipher found.

    Keyword arguments:
    initial -- starting guess as to the cipher (if omitted, the search
               starts at a randomly chosen cipher).
    choices -- at each step, choose the next state in the search
               randomly from this many top candidates (default: 10).

    """
    if initial is None:
        initial = list(LETTERS)
        shuffle(initial)

    # Current best cipher and its score
    best_cipher = initial
    best_score = score_fun(decipher(ciphertext, initial))

    # List of all possible swaps of two letters in the cipher.
    swaps = list(combinations(range(len(LETTERS)), 2))

    def neighbours():
        # Yield neighbouring ciphers (those that differ from the
        # current best cipher by a single swap of letters) that are
        # better than the current cipher.
        for i, j in swaps:
            cipher = list(best_cipher)
            cipher[i], cipher[j] = cipher[j], cipher[i]
            score = score_fun(decipher(ciphertext, cipher))
            if score > best_score:
                yield score, cipher

    while True:
        try:
            best_score, best_cipher = choice(nlargest(choices, neighbours()))
        except IndexError:
            # No swap yielded an improved score.
            best_cipher = ''.join(best_cipher)
            return best_score, best_cipher, decipher(ciphertext, best_cipher)


def find_cipher2(ciphertext, score_funs, initial=None, choices=10):
    """Attempt to decrypt ciphertext, using the score functions (with weights)
     in score_fun to score the candidate plaintexts. Return a tuple
    (score, cipher, plaintext) for the best cipher found.

    Keyword arguments:
    initial -- starting guess as to the cipher (if omitted, the search
               starts at a randomly chosen cipher).
    choices -- at each step, choose the next state in the search
               randomly from this many top candidates (default: 10).

    """
    if initial is None:
        initial = list(LETTERS)
        shuffle(initial)

    # Current best cipher and its score
    best_cipher = initial
    best_score = sum([score_fun(decipher(ciphertext, initial))/i for score_fun, i in score_funs])

    # List of all possible swaps of two letters in the cipher.
    swaps = list(combinations(range(len(LETTERS)), 2))

    def neighbours():
        # Yield neighbouring ciphers (those that differ from the
        # current best cipher by a single swap of letters) that are
        # better than the current cipher.
        for i, j in swaps:
            cipher = list(best_cipher)
            cipher[i], cipher[j] = cipher[j], cipher[i]
            score = sum([score_fun(decipher(ciphertext, cipher))/i for score_fun, i in score_funs])
            if score > best_score:
                yield score, cipher

    while True:
        try:
            best_score, best_cipher = choice(nlargest(choices, neighbours()))
        except IndexError:
            # No swap yielded an improved score.
            best_cipher = ''.join(best_cipher)
            return best_score, best_cipher, decipher(ciphertext, best_cipher)

