import re
import sys

filename = str(sys.argv[1])
mainTower = str(sys.argv[2])
file = open(filename,'r')
towers = {}
weights = {}
for line in file:
    line = line.strip('\n')
    keys = re.split('\W+',line)
    if len(keys) == 3:
        del keys[2]
    weights[keys[0]] = int(keys[1])
    del keys[1]
    towers[keys[0]] = keys[1:]

def weightSum(tower):
    weight = weights[tower]
    for i in towers[tower]:
        weight += weightSum(i)
    return weight

def getAllWeights(tower):
    baseWeights = []
    for i in towers[tower]:
        weight = weightSum(i)
        baseWeights.append(weight)
    return baseWeights


def getTower(tower):
    baseWeights = []
    found,finalWeight,ftower = False,0,''
    for i in towers[tower]:
        found,finalWeight, ftower = getTower(i)
        if found == True:
            break;
        weight = weightSum(i)
        baseWeights.append(weight)
        finalWeight = baseWeights
        ftower = i
        baseWeights = set(baseWeights)
        baseWeights = list(baseWeights)
        if (len(baseWeights) == 2):
            found = True
            break;
    return found, finalWeight, ftower

def getParent(tower):
    for i in towers:
        if tower in towers[i]:
            return i

def getWeight(mainTower):
    found,weight,tower = getTower(mainTower)
    weight = weightSum(tower)
    parent = getParent(tower)
    allWeights = getAllWeights(parent)
    required = 0
    for i in allWeights:
        if i != weight:
            required = weights[tower] + i - weight
    return required

print getWeight(mainTower)
