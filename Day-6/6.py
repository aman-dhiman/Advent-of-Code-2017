import sys

filename = str(sys.argv[1])
file = open(filename,'r')

line = file.readline().strip('\n')
nums = line.split('\t')
for index,num in enumerate(nums):
    nums[index] = int(num)

def getMax(list):
    return max(list),list.index(max(list))

numBanks = len(nums)
patterns = []
match = False
index = 0
steps = 0 #total steps
last = 0
pattern = ()
while match == False:
    high,index = getMax(nums)
    nums[index] = 0
    for i in range(high):
        index+=1
        if index >= len(nums):
            index = 0
        nums[index]+=1
    steps+=1
    pattern = tuple(nums)
    if pattern in patterns:
        match = True
        last = patterns.index(pattern)
    else:
        patterns.append(pattern)
print steps,steps-last-1 #steps from last occurence
