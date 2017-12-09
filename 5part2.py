import sys

filename = str(sys.argv[1])
file = open(filename,'r')
maze = []
for line in file:
    line = int(line.strip('\n'))
    maze.append(line)

min = 0
max = len(maze)-1
steps = 0
index = 0
while index >= min and index <= max:
    if maze[index] >= 3:
        maze[index]-=1
        index = maze[index]+1+index
    else:
        maze[index]+=1
        index = maze[index]-1+index
    steps+=1
print steps
