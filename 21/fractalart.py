import copy



rawrules = []
matcher = {}
with open ('c:/Users/derwin/AOC/21/input', 'r') as f:
    for line in f:
        rawrules.append(line)
print("Start")
for row in rawrules:
    row = row.strip().split(' => ')
    matcher[row[0]] = row[1]
    


def rotate(grid):
    grid = grid.split('/')
    gl = len(grid)
    outgrid = copy.deepcopy(grid)
    for x in range(0,gl):
        outgrid[x] = ''
        for y in range(0,gl):
            outgrid[x] += grid[y][gl - x - 1]
    return '/'.join(outgrid)

def hflip(grid):
    grid = grid.split('/')
    gl = len(grid)
    outgrid = copy.deepcopy(grid)
    for x in range(0,gl):
        outgrid[x] = ''
        for y in range(gl-1,-1,-1):
            outgrid[x] += grid[x][y]
    return '/'.join(outgrid)
    

def vflip(grid):
    grid = grid.split('/')
    gl = len(grid)
    outgrid = copy.copy(grid)
    for x in range(gl - 1,-1, -1):
        outgrid[x] = ''
        for y in range(0, gl):
            outgrid[x] += grid[gl - x - 1][y]
    return '/'.join(outgrid)

def getdivisor(pattern):
    for i in [2,3]:
        if len(pattern.split('/')) % i == 0:
            return i


def matchpattern(pattern):
    for i in range(0,4):
        pattern = rotate(pattern)
        if pattern in matcher:
            return matcher[pattern]
        pattern = hflip(pattern)
        if pattern in matcher:
            return matcher[pattern]
        pattern = vflip(pattern)
        if pattern in matcher:
            return matcher[pattern]
        pattern = hflip(pattern)
        if pattern in matcher:
            return matcher[pattern]
        pattern = vflip(pattern) # back to square one, ready to rotate again
        
#print(rotate('#./..'))
#print(hflip('#../.#./..#'))
#print(hflip('#./#.'))
#print(vflip('#../.#./..#'))
#print(getdivisor('##/..'))



# .#.
# ..#
# ###
#
# ##.
# #.#
# #..
#

def doiteration(pattern):
    # takes a '/' separated string, returns a larger one representing a larger grid
    length = len(pattern.split('/'))
    div = getdivisor(pattern)
    outdiv = div + 1
    numsubs = length//div
    outputsize = numsubs * (div + 1)
    outpattern = outpattern = ['' * outputsize] * outputsize
    pattern = pattern.split('/')
    
    for y in range(0,numsubs):
        for x in range(0,numsubs):
            subpattern = ['' * div] * div
            for p in range(0,div):
                for q in range(0,div):
                    # print(x,y,p,q)
                    subpattern[p] += pattern[y * div  + p][x * div + q]
            newpattern = matchpattern('/'.join(subpattern))
            for p in range(0,outdiv):
                for q in range(0,outdiv):
                    outpattern[outdiv * y + p] += newpattern.split('/')[p][q]
    return '/'.join(outpattern)
    


pattern = '.#./..#/###'
print(pattern)
for i in range(0,18):
    pattern = doiteration(pattern)
#    for x in pattern.split('/'):
#        print(x)
    print("-----------------", i)
#print(pattern)

count = 0
for x in pattern:
    if x=='#':
        count+=1

print(count)
