import sys

# sys.setrecursionlimit(20000)
filename = str(sys.argv[1])
file = open(filename, 'r')

comm = {}
groups = []

def getmoreids (comm, cur, ids):
    moreids = ids
    for elem in comm[cur]:
        if elem not in ids:
            ids.append(elem)
            moreids = getmoreids(comm, elem, ids)
    return moreids

def getallids (comm, id):
    ids = [id]
    for cur in comm[id]:
        if cur not in ids:
            ids.append(cur)
            ids = getmoreids(comm, cur, ids)

    return ids

for line in file:
    line = line.strip('\n').translate(None, '-<>,').split(' ')
    del line[1]
    for index,id in enumerate(line):
        line[index] = int(id)
    comm[line[0]] = line[1:]
# for index,id in enumerate(comm):

for index in range(len(comm)):
    glist = sorted(getallids(comm,index))
    if glist not in groups:
        groups.append(glist)
print len(getallids(comm,0)), len(groups)
# print sorted(getallids(comm,3))
