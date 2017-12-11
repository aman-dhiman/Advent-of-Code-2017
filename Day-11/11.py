import sys

filename = str(sys.argv[1])
file = open(filename,'r')

line = file.readline().strip('\n').split(',')
def getPos(step,x,y):
    if step == 'n':
        y += 1
    elif step == 'ne':
        x+=1
        y+=.5
    elif step == 'nw':
        x-=1
        y+=.5
    elif step == 's':
        y-=1
    elif step == 'se':
        x+=1
        y-=.5
    elif step == 'sw':
        x-=1
        y-=.5
    return x,y
def getshortpath(x,y):
    step = 0
    curx = 0
    cury = 0
    if x>0 and y>0:
        while (curx != x and cury != y):
            step+=1
            curx+=1
            cury+=.5
        if x>curx:
            step = step+abs(x-curx)
        elif y>cury:
            step = step+abs(y-cury)
    elif x>0 and y<0:
        while (curx != x and cury != y):
            step+=1
            curx+=1
            cury-=.5
        if x>curx:
            step = step+abs(x-curx)
        elif y<cury:
            step = step+abs(y-cury)
    elif x<0 and y<0:
        while (curx != x and cury != y):
            step+=1
            curx-=1
            cury-=.5
        if x<curx:
            step = step+abs(x-curx)
        elif y<cury:
            step = step+abs(y-cury)
    elif x<0 and y>0:
        while (curx != x and cury != y):
            step+=1
            curx-=1
            cury+=.5
        if x<curx:
            step = step+abs(x-curx)
        elif y>cury:
            step = step+abs(y-cury)
    return int(step)

x = 0
y = 0
furthest = 0

for step in line:
    x,y = getPos(step,x,y)
    if getshortpath(x,y) > furthest:
        furthest = getshortpath(x,y)

print getshortpath(x,y), furthest
