import sys

filename = str(sys.argv[1])
file = open(filename,'r')
summ = 0

for line in file:
    line = line.strip('\n')
    line = line.split('\t')
    nums = []
    for num in line:
        nums.append(int(num))
    maxval = max(nums)
    minval = min(nums)
    diff = maxval-minval
    summ+=diff
print summ
