import sys

filename = str(sys.argv[1])
file = open(filename,'r')

line = file.readline()
line = line.strip('\n')
index = 0
summ = 0
length = len(line)
for cur,i in enumerate(line):
    i = int(i)
    index = cur+(length/2)
    if index > (length-1):
        index -= length
    if i == int(line[index]):
        summ+=i
print summ
