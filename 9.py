import sys

filename = str(sys.argv[1])
file = open(filename, 'r')

line = file.readline()
line = line.strip('\n')
index = 0
garbage = False
ignore = 1
level = 0
score = 0
summ = 0
for cur,char in enumerate(line):
    ignore+=1
    if ignore >= 2 and garbage == True and char != '!' and char != '>':
        summ+=1
    if ignore >= 2 and garbage == True and char == '>':
        garbage = False
    elif ignore >= 2 and char == '!':
        ignore = 0
    elif ignore >= 2 and garbage == False:
        if char == '{':
            level+=1
        elif char == '}':
            score+=level
            level-=1
        elif char == '<':
            garbage = True
print score, summ
