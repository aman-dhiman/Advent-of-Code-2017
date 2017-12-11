import sys

filename = str(sys.argv[1])
file = open(filename, 'r')

def gethex(int):
    return "%0.2X"%int

cur = 0
lengths = []
skip = 0
line = file.readline()
line = line.strip('\n')
lengths = list(line)
for index,i in enumerate(lengths):
    lengths[index] = ord(i)
morelen = [17, 31, 73, 47, 23]
lengths+=morelen
numlist = []
for i in range(256):
    numlist.append(i)
run = 0
while run < 64:
    for indexi,i in enumerate(lengths):
        length = lengths[indexi]
        partlist = numlist[cur:length+cur]
        iteration = cur + length
        if iteration > 255:
            while iteration > 255:
                iteration = iteration-256
            for e in range(iteration):
                partlist.append(numlist[e])
        # print partlist
        partlist = list(reversed(partlist))
        # print partlist
        for indexj,j in enumerate(partlist):
            findex = cur + indexj
            while findex > 255:
                findex = findex-256
            numlist[findex] = partlist[indexj]
        cur = cur + length + skip
        while cur > 255:
            cur = cur-256
        skip+=1
        # print cur,skip,length,numlist
    run+=1
start = 0
end = 16
hashes = []
for i in range(16):
    templist = numlist[start:end]
    orvalue = 0
    for j in range(15):
        if j == 0:
            orvalue = templist[j] ^ templist[j+1]
        else:
            orvalue = orvalue ^ templist[j+1]
    hashes.append(orvalue)
    start+=16
    end+=16
hexes = ""
for i in hashes:
    hexval = gethex(i)
    hexes+=hexval
print hexes.lower()
