class Loop(object):
    contents = []
    size = 0

    def __init__(self, size):
        self.contents = list(range(0,size))
        self.size = size

    def get(self):
        return self.contents

# Move the whole ring so our start position is zero
    def leftshift(self, offset):
        offset = offset % self.size
        firsthalf = self.contents[offset:]
        secondhalf = self.contents[:offset]
        return firsthalf + secondhalf


    def rightshift(self, offset, ring):
        offset = offset % self.size
        firsthalf = ring[-offset:]
        secondhalf = ring[:-offset]
        return firsthalf + secondhalf

    def simpleReverse(self,start, length):
        rotato = self.leftshift(start)
        selection = rotato[:length]
        rev = selection[::-1]
        rotato[:length] = rev
        self.contents = self.rightshift(start,rotato)
        
def densifyBlock(block):
    return block[0] ^ block[1] ^ block[2] ^ block[3] ^ block[4] ^ block[5] ^ block[6] ^ block[7] ^ block[8] ^ block[9] ^ block[10] ^ block[11] ^ block[12] ^ block[13] ^ block[14] ^ block[15]

        
listLength = 256
rounds = 64
blocksize = 16
totalOnes = 0
suffix = [17, 31, 73, 47, 23]

# Now we do it for the memory

thegrid = []
for row in range(0,128):
    input = 'ljoxqyyw-' + str(row)
#    input = 'flqrgnkx-' + str(row) # test input to validate our approach
    # so, we first convert our input into ASCII numbers

    input = [ord(x) for x in input] + suffix
    rope = Loop(listLength)
    skip = 0
X    position = 0
    for i in range(0,rounds):
        for j in input:
            rope.simpleReverse(position,j)
            position = (position + j + skip) % listLength
            skip = skip + 1

            sparseHash = rope.get()
            denseHash = ''

            for k in range(0,listLength//blocksize):
                output = densifyBlock(sparseHash[k * blocksize:k*blocksize + blocksize])
                denseHash = denseHash + format(output,'08b')
                
    thegrid.append([int(i) for i in denseHash])
    for i in denseHash:
        totalOnes += int(i)

print("Number of filled cells:", totalOnes)

# Part II: the groups!



def crawl(grid,x,y, groupnum):
    grid[y][x] = groupnum

    if x > 0 and thegrid[y][x-1] != 0 and grid[y][x-1] == 0:
        crawl(grid,x-1,y,groupnum)
    if x < len(grid[0]) - 1 and thegrid[y][x+1] != 0 and grid[y][x+1] == 0:
        crawl(grid,x+1,y,groupnum)
    if y > 0 and thegrid[y-1][x] != 0 and grid[y-1][x] == 0:
        crawl(grid,x,y-1,groupnum)
    if y < len(grid) - 1 and thegrid[y+1][x] != 0 and grid[y+1][x] == 0:
        crawl(grid,x,y+1,groupnum)

    
groupgrid = [[0 for i in range(0,(len(thegrid[0])))] for j in range(0,len(thegrid))] # copy the grid, but as zeroes
groupcount = 1 # 0 signifies free space, we count from 1

for y in range(0,len(thegrid)):
    for x in range(0,len(thegrid[0])):
        if thegrid[y][x] == 0:
            groupgrid[y][x] = 0
        else:
            if groupgrid[y][x] == 0:
                crawl(groupgrid,x,y,groupcount)
                groupcount += 1

groupset = set()
for x in groupgrid:
    groupset |= set(x)
print("Total sets (including zero): ", len(groupset))                   
