import sys

filename = str(sys.argv[1])
file = open(filename,'r')

valid = 0
chars1 = {}
chars2 = {}
for line in file:
    line = line.strip(' \n')
    words = line.split(' ')
    match = False
    for index1,word1 in enumerate(words):
        for char1 in word1:
            chars1[char1] = chars1.get(char1,0) +1
        for index2,word2 in enumerate(words):
            if index1!=index2:
                for char2 in word2:
                    chars2[char2] = chars2.get(char2,0) +1
                if chars1 == chars2:
                    match = True
                    chars2.clear()
                    break
                chars2.clear()
        chars1.clear()
        if match == True:
            break;
    if match == False:
        valid+=1
print valid
