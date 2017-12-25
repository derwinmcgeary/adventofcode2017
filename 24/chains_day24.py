import copy

filename = 'C:/Users/derwin/AOC/24/input'
#filename = 'C:/Users/derwin/AOC/24/testinput' 

with open(filename, 'r') as f:
    connections = f.readlines()
connections = [x.strip() for x in connections]

connections = [list(map(int,x.split('/'))) for x in connections]
print(connections)

def findmatching(freeend, partslist):
    possibilities = []
    for x in partslist:
        if freeend in x:
            possibilities.append(x)
    return possibilities

def getchains(connectors, chain):
    global chainlist
    connectors = copy.copy(connectors)
    chain = copy.copy(chain)
    chainend = chain[-1][1] # second item in the end of chain
    if len(connectors) == 0:
        return

    for x in findmatching(chainend,connectors):
        newconnectors = copy.copy(connectors)
        newconnectors.remove(x)
        if x[1] == chainend:
            x = x[::-1]
        newchain = copy.copy(chain)
        newchain.append(x)
        chainlist.append(newchain)
        getchains(newconnectors, newchain)

def showchains(chainlist):
    for x in chainlist:
        print(x)

def sumchain(chain):
    total = 0
    for x in chain:
        total += sum(x)
    return total

def findmax(chainlist):
    maxval = 0
    maxindex = 0

    for i in range(0,len(chainlist)):
        curval = sumchain(chainlist[i])
        if curval > maxval:
            print(chainlist[i])
            maxval = curval
            maxindex = i
    return chainlist[maxindex], maxval

def findlongest(chainlist):
    maxlen = 0
    maxchains = []
    for x in chainlist:
        if len(x) > maxlen:
            maxlen = len(x)
            maxchains = []
            maxchains.append(x)
        if len(x) == maxlen:
            maxchains.append(x)
    return maxchains
        

chainlist = []

startpos = [[0,0]]
    
print("CHAINS")
getchains(connections,startpos)
print(findmax(chainlist))

cl = findlongest(chainlist)
print(findmax(cl))
