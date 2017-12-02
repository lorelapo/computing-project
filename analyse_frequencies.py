import operator

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

def getFrequencyString(message):
    letterCount=getLetterCount(message)
    sortedDict = sorted(letterCount.items(), key=operator.itemgetter(1))
    sortedDict.reverse()
    return sortedDict

def getAlphabet(freqString):
    return ''.join([e[0] for e in freqString])

with open('.idea/input.txt', 'r') as input:
    data = input.read()

sFreq = getFrequencyString(data)
alpha = getAlphabet(sFreq)
print(sFreq)
print(alpha)
