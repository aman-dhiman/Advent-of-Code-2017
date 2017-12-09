import sys

filename = str(sys.argv[1])
file = open(filename,'r')

line = file.readline()
line = line.strip('\n')
index = 0
summ = 0
for cur,i in enumerate(line):
    i = int(i)
    index = cur+1
    if index == len(line):
        index = 0
    if i == int(line[index]):
        summ+=i
print summ
