with open('C:/Users/derwin/AOC/7/input', 'r') as f:
    content = f.readlines()
content = [x.strip() for x in content]

lineage = {}
weights = {}
kids = {}
# names = []

for x in content:
    parent = x.split(' -> ')[0]
    if len(x.split(' -> ')) > 1:
        childs = x.split(' -> ')[1]
        children = childs.split(', ')
    else:
        children = "X"
    guardian = parent.split(' ')[0]
    weight = int(parent.split(' ')[1][1:-1])

    for i in children:
        lineage[i] = guardian
    kids[guardian] = children
    weights[guardian] = weight


for x in kids:
    if x not in lineage:
        root = x

print("Root node is ", root)

def sumTotal(node):
    totalWeight = weights[node]
    if kids[node] == 'X':
        return totalWeight
    else:
        for x in kids[node]:
            totalWeight = totalWeight + sumTotal(x)
        return totalWeight

def oddOneOut(subWeights):
    countsList = {}
    for x in subWeights:
        countsList[subWeights[x]] = 0
    for x in subWeights:
        countsList[subWeights[x]] = countsList[subWeights[x]] + 1
    if len(countsList) == 1:
       return 'balanced', sorted(countsList)[0], 0
    for x in countsList:
        if countsList[x] == 1:
            oddweight = x

    for x in subWeights:
        if subWeights[x] != oddweight:
            delta = oddweight - subWeights[x]
        
    for x in subWeights:
        if subWeights[x] == oddweight:
            return x, subWeights[x], delta


def trackUnbalance(node):
    subweights = {}
    if kids[node] == 'X':
        return 'Done!'
    for y in kids[node]:
        subweights[y] = sumTotal(y)
    odd, weight, delta = oddOneOut(subweights)

    if odd == 'balanced':
        print('previous line shows correct weight!')
    else:
        print(odd, weight, weights[odd] ,delta, weights[odd] - delta)
        trackUnbalance(odd)
trackUnbalance(root)

