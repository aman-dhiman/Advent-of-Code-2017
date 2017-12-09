import sys

filename = str(sys.argv[1])
file = open(filename,'r')

valid = 0
for line in file:
    line = line.strip(' \n')
    words = line.split(' ')
    match = False
    for index1,word1 in enumerate(words):
        for index2,word2 in enumerate(words):
            if index1!=index2 and word1==word2:
                match = True
                break
        if match == True:
            break
    if match == False:
        valid+=1
print valid
