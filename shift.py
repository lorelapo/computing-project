import operator

alphabet=' abcdefghijklmnopqrstuvwxyz'
key=' nutiyvxqflbcjrodhkaewspzgm'
plaintext="hello world"

def shift(plaintext, key, alphabet):
    keyIndices = [alphabet.index(k.lower()) for k in plaintext]
    return ''.join(key[keyIndex] for keyIndex in keyIndices)

cypher = shift(plaintext, key, alphabet)

print(plaintext)
print(cypher)

cryptext="AKBP AKBP PSKFG KUC ZWJSQ KB SADSFCF LVC HVCIUVH GC AIOV CT BSL OZCHVSG HVKH VS GDSBH KZZ VWG ACBSP WB CFQSF HC CMHKWB HVSA VWG CBZP KAMWHWCB LKG HC MS KZLKPG LSZZ QFSGGSQ VS QWQ BCH OKFS TCF VWG GCZQWSFG KBQ HVS HVSKHFS QWQ BCH KAIGS VWA HVS CBZP HVWBU WB TKOH VS HVCIUVH KBPHVWBU CT LKG HC QFWJS CIH KBQ GVCL K BSL GIWH CT OZCHVSG VS VKQ K OCKH TCF SJSFP VCIF CT HVS QKP KBQ KG CBS LCIZQ GKP CT K YWBU VS WG WB VWG OKMWBSH GC CBS OCIZQ GKP CT VWA HVS SADSFCF WG WB VWG QFSGGWBU FCCA"
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def getCount(message):
    count=0
    for letter in message.upper():
        if letter in LETTERS:
            count +=1
    return count

def getLetterCount(message):
    totalcount=getCount(message)
    letterCount = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0,
                 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}
    for letter in message.upper():
        if letter in LETTERS:
            letterCount[letter] += 100/totalcount
    return letterCount

def getFrequencyString(message):
    lettercount=getLetterCount(message)
    countstring=[]
    for letter in LETTERS:
        countstring.append("letter, lettercount[letter]")
    return countstring


englishLetterFreq = {'E': 12.70, 'T': 9.06, 'A': 8.17, 'O': 7.51, 'I': 6.97, 'N': 6.75, 'S': 6.33, 'H': 6.09, 'R': 5.99, 'D': 4.25, 'L': 4.03, 'C': 2.78, 'U': 2.76, 'M': 2.41, 'W': 2.36, 'F': 2.23, 'G': 2.02, 'Y': 1.97, 'P': 1.93, 'B': 1.29, 'V': 0.98, 'K': 0.77, 'J': 0.15, 'X': 0.15, 'Q': 0.10, 'Z': 0.07}
ETAOIN = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'
frequencies=getFrequencyString(cryptext)
print(frequencies)



