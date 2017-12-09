import sys

num = int(sys.argv[1])

def totalinstep(step):
    summ = 1
    for i in range(1,step):
        summ+= i*8
    return summ

def getstep(num):
    step = 1
    while totalinstep(step)<num:
        step+=1
    if step == 1:
        return 1,1,1
    return step,totalinstep(step-1)+1,totalinstep(step)

# def stepside(step):
#     return ((step-1)*2)+1

def getdist(num):
    step,low,high = getstep(num)
    div = (((high-low)+1)/4)+1
    cur = low
    top = []
    bottom = []
    left = []
    right = []
    cent = (div-1)/2
    diff = 0
    for i in range(0,div):
        if i == div-1:
            right.append(high)
        else:
            right.append(cur+div-i-2)
    cur = cur+div-2
    for i in range(0,div):
        top.append(cur+div-i-1)
    cur = cur+div-1
    for i in range(0,div):
        left.append(cur+i)
    cur = cur+div-1
    for i in range(0,div):
        bottom.append(cur+i)
    if num in right:
        index = right.index(num)
    elif num in top:
        index = top.index(num)
    elif num in left:
        index = left.index(num)
    elif num in bottom:
        index = bottom.index(num)
    diff = abs(index-cent)
    diff+= step-1
    return diff

print getdist(num)
# step = 1
# nums = []
# summ = 0
# for i in range(0,100):
#     side = (i*2)+1
#     if side == 1:
#         nums.append(1)
#     else:
#         nums.append((side*2)+((side-2)*2))
#     summ += nums[i]
# print nums, summ
