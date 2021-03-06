#===============================================================================
# the script contains functions to clean and separate texts
# we are using Willliam Henry Harrison's inauguation speech
# data: 3/23/2016
#===============================================================================

from urllib.request import urlopen
from bs4 import BeautifulSoup
from pprint import pprint
import re
import string
import operator


def cleanInput(input):
    input = re.sub("\n+", " ", input).lower()
    input = re.sub("\[[0-9]*\]", " ", input)
    input = re.sub(" +", " ", input)
    input = bytes(input, 'UTF-8')
    input = input.decode("ascii", "ignore")
    cleanInput = []
    input = input.split(sep=" ")
    for item in input:
        item = item.strip(string.punctuation)
        if len(item) > 1 or (item.lower() == 'a' or item.lower() == 'i'):
            cleanInput.append(item)
    return cleanInput

def ngrams(input, n):
    input = cleanInput(input)
    output = {}
    for i in range(len(input)-n+1):
        ngramTemp = " ".join(input[i:i+n])
        if ngramTemp not in output:
            output[ngramTemp] = 0
        output[ngramTemp] += 1
    return output

if __name__ == '__main__':
    content = str(urlopen("http://pythonscraping.com/files/inaugurationSpeech.txt").read(), 'UTF-8')
    ngrams = ngrams(content, 2)
    
    # this will sort a dictionary using a built-in function, returning with a list
    sortedNGrams = sorted(ngrams.items(), key=operator.itemgetter(1), reverse=True)
    
    pprint(sortedNGrams[:10])
    print("count of grams: %d", len(sortedNGrams))