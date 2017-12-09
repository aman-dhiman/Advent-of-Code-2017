import sys

filename = str(sys.argv[1])
file = open(filename,'r')

registers = {}
instructions = []

for line in file:
    line = line.strip('\n')
    line = line.split(' ')
    del line[3]
    registers[line[0]] = 0
    line[2] = int(line[2])
    line[5] = int(line[5])
    instructions.append(tuple(line))

def ifs(reg, query, value):
    if query == ">":
        return registers[reg]>value
    elif query == "<":
        return registers[reg]<value
    elif query == ">=":
        return registers[reg]>=value
    elif query == "<=":
        return registers[reg]<=value
    elif query == "==":
        return registers[reg]==value
    elif query == "!=":
        return registers[reg]!=value

def modify(reg, query, value):
    if query == "dec":
        registers[reg]-=value
    elif query == "inc":
        registers[reg]+=value

def perform():
    maxval = 0
    for i in instructions:
        if ifs(i[3],i[4],i[5]):
            modify(i[0],i[1],i[2])
            if max(registers.values()) > maxval:
                maxval = max(registers.values())
    return maxval

maxval = perform() #Max value that occured at any point
print max(registers.values()), maxval
