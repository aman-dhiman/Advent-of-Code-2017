import sys

filename = str(sys.argv[1])
file = open(filename, 'r')

cur = 0
lengths = []
skip = 0
line = file.readline()
line = line.strip('\n')
lengths = line.split(',')
lengthSize = len(lengths)
numlist = []
for index,i in enumerate(lengths):
    lengths[index] = int(lengths[index])
for i in range(256):
    numlist.append(i)
for indexi,i in enumerate(lengths):
    length = lengths[indexi]
    partlist = numlist[cur:length+cur]
    if cur+length > 255:
        iteration = cur+length-256
        for e in range(iteration):
            partlist.append(numlist[e])
    # print partlist
    partlist = list(reversed(partlist))
    # print partlist
    for indexj,j in enumerate(partlist):
        findex = cur + indexj
        if findex > 255:
            findex = findex-256
        numlist[findex] = partlist[indexj]
    cur = cur + length + skip
    if cur > 255:
        cur = cur-256
    skip+=1
    # print cur,skip,length,numlist
print numlist[0]*numlist[1]
