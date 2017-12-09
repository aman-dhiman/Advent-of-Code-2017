import sys

filename = str(sys.argv[1])
file = open(filename,'r')
summ = 0

for line in file:
    line = line.strip('\n')
    nums = line.split('\t')
    quo = 0
    for index1, num1 in enumerate(nums):
        if quo != 0: break
        num1 = int(num1)
        for index2, num2 in enumerate(nums):
            num2 = int(num2)
            if index2 != index1:
                if num2/num1 != 0 and num2%num1 == 0:
                    quo = num2/num1
                    break
                elif num1/num2 != 0 and num1%num2 == 0:
                    quo = num1/num2
                    break

    summ+=quo
print summ
