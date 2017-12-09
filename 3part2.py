import numpy
import sys

num = int(sys.argv[1])

array = numpy.zeros((9,9))

def right(x,y):
    return x+1,y
def up(x,y):
    return x,y-1
def left(x,y):
    return x-1,y
def down(x,y):
    return x, y+1
def getSum(array,x,y):
    summ = 0
    a,b = array.shape
    for i in range(x-1,x+2):
        for j in range(y-1,y+2):
            if j < a and i < b and i >= 0 and j >= 0:
                summ+=array[j,i]
    return summ

def fillArray(array):
    cent = (array.shape[0]-1)/2
    steps = cent*4+1
    turn = 0
    x = cent
    y = cent
    array[y,x]=1
    move = 2
    for i in range(0,steps):
        if turn%4 == 0:
            for j in range(move/2):
                x,y = right(x,y)
                if not(i == (steps-1) and j == ((move/2)-1)):
                    array[y,x] = getSum(array,x,y)
        elif turn%4 == 1:
            for j in range(move/2):
                x,y = up(x,y)
                array[y,x] = getSum(array,x,y)
        elif turn%4 == 2:
            for j in range(move/2):
                x,y = left(x,y)
                array[y,x] = getSum(array,x,y)
        elif turn%4 == 3:
            for j in range(move/2):
                x,y = down(x,y)
                array[y,x] = getSum(array,x,y)
        move+=1
        turn+=1
    return array

fillArray(array)
closeval = 0
index = 0
for i in array:
    for j in i:
        if j > num:
            if index == 0:
                closeval = j
            elif j < closeval:
                closeval = j
            index+=1
print int(closeval)
