import string
import operator

englishLetterFreq = \
    {'E': 12.70, 'T': 9.06, 'A': 8.17, 'O': 7.51, 'I': 6.97, 'N': 6.75, 'S': 6.33, 'H': 6.09, 'R': 5.99, 'D': 4.25, 'L': 4.03, 'C': 2.78, 'U': 2.76, 'M': 2.41, 'W': 2.36, 'F': 2.23, 'G': 2.02, 'Y': 1.97, 'P': 1.93, 'B': 1.29, 'V': 0.98, 'K': 0.77, 'J': 0.15, 'X': 0.15, 'Q': 0.10, 'Z': 0.07}

def shift(plaintext, key, alphabet):
    keyIndices = [alphabet.index(k.lower()) for k in plaintext]
    return ''.join(key[keyIndex] for keyIndex in keyIndices)

def getCount(sInput):
    count = 0
    for letter in sInput.lower():
        count +=1
    return count

def getLetterCount(sInput):
    totCount = getCount(sInput)
    letCount = {'a' : 0}
    for e in sInput.lower():
        if e in letCount.keys():
            letCount[e] += 100 / totCount
        else:
            letCount[e] = 100 / totCount
    return letCount

def getTrigramCount(sInput):
    totCount = getCount(sInput)-2
    trigCount = {'abc' : 0}
    for e in range(0, totCount):
        trig = str(sInput[e:e+3])
        if trig in trigCount.keys():
            trigCount[trig] += 1
        else:
            trigCount[trig] = 1
    return trigCount

def getTrigramString(sInput):
    trigCount = getTrigramCount(sInput)
    sortedDict = sorted(trigCount.items(), key=operator.itemgetter(1))
    sortedDict.reverse()
    return sortedDict

def getFrequencyString(message):
    letterCount = getLetterCount(message)
    sortedDict = sorted(letterCount.items(), key=operator.itemgetter(1))
    sortedDict.reverse()
    return sortedDict

def cleanData(data):
    cDat = ''
    alphabet = ' '+string.ascii_lowercase
    for e in data:
        if e in alphabet:
            cDat += e
    return cDat

def freqProd(f1, f2):
    prod = 0
    for i in range(0, f1.length()):
        prod += f1[i][1] * f2[i][1]
    return prod

def getAlphabet(freqString):
    return ''.join([e[0] for e in freqString])
