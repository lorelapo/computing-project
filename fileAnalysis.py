import freqAnalysis
import json

def analyseFileAlphabet(inname, outname):
    with open(inname, 'r') as input:
        data = input.read()
    sfreq = freqAnalysis.getFrequencyString(freqAnalysis.cleanData(data))
    with open(outname, 'w') as output:
        json.dump(sfreq, output)

def getCharFreq(inname):
    with open(inname, 'r') as input:
        data = json.load(input)
    return data

def analyseFileTrigram(inname, outname):
    with open(inname, 'r') as input:
        data = input.read()
    sfreq = freqAnalysis.getTrigramString(freqAnalysis.cleanData(data))
    with open(outname, 'w') as output:
        json.dump(sfreq, output)

def getTrigramFreq(inname):
    with open(inname, 'r') as input:
        data = json.load(input)
    return data