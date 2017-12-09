import re
import sys

filename = str(sys.argv[1])
file = open(filename,'r')
words = {}
for line in file:
    line = line.strip('\n')
    keys = re.split('\W+|\d+',line)
    for i in keys:
        words[i] = words.get(i,0)+1
for i in words:
    if words[i] == 1:
        print i
