from collections import defaultdict, Counter
from sys import stdin
import codecs

def word_count():
    wordDict = defaultdict(int)
    filename = open("Shakespeare.txt","r").read()
    filename = filename.lower()
    for ch in '"''!@#$%^&*()-_=+,<.>/?;:[{]}~`\|':
        filename = filename.replace(ch," ")
    for word in filename.split():
        if word not in wordDict:
            wordDict[word] = 1
        else:
            wordDict[word] = wordDict[word] + 1
    print(wordDict["the"])


word_count()
