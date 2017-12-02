import fileAnalysis

fileAnalysis.analyseFileTrigram('.idea/input.txt', '.idea/eng.dat')

freq = fileAnalysis.getTrigramFreq('.idea/eng.dat')

print(freq)