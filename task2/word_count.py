from collections import defaultdict, Counter
from sys import stdin
import json
import pydoop.hdfs as hdfs


def word_count():
    wordDict = defaultdict(int)
    filename = open("/home/marcus/tasks/Shakespeare.txt","r").read()
    filename = filename.lower()
    for ch in '"''!@#$%^&*()-_=+,<.>/?;:[{]}~`\|':
        filename = filename.replace(ch," ")
    for word in filename.split():
        if word not in wordDict:
            wordDict[word] = 1
        else:
            wordDict[word] = wordDict[word] + 1
    #print(wordDict["the"])

    with open('/home/marcus/Mindbender_BD/task2/python_output.txt', 'w') as file:
         file.write(json.dumps(wordDict))

    from_path = "/home/marcus/Mindbender_BD/task2/python_output.txt"
    to_path ='hdfs://localhost:9000/task2/outfile.txt'
    hdfs.put(from_path, to_path)

    

word_count()
