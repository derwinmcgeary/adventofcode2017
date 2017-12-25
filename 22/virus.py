grid = {} # tuple(x,y) : '#' or '.'
current = tuple([0,0])
direction = tuple([0,1]) # pointing up
caused = 0

def turn(dir):
    global direction
    #print("olddir", direction)
    turns = {'left': [ -1, 1], 'right': [1,-1]}
    direction = tuple([turns[dir][0] * direction[1], turns[dir][1] * direction[0]])
    #print("newdir", direction)


def printgrid(gridsize):
    for j in range(-1 * gridsize,gridsize):
        outputrow = ''
        for i in range(-1 * gridsize,gridsize):
            coordinate = tuple([i, -1 * j])
            if coordinate == current:
                outputrow += '['
            else:
                outputrow += ' '
            if coordinate in grid:
                outputrow += grid[coordinate]
            else:
                outputrow += '.'
            if coordinate == current:
                outputrow += ']'
            else:
                outputrow += ' '
        print(outputrow)
def burst():
    sequ = {'.' : 'W', 'W': '#', '#' : 'F', 'F': '.'}
    global grid
    global current
    global direction
    global caused
    if current not in grid:
        grid[current] = '.'
    if grid[current] == '.':
        turn('left')
    if grid[current] == 'W':
        caused += 1
    if grid[current] == '#':
        turn('right')
    if grid[current] == 'F':
        turn('right')
        turn('right')
    grid[current] = sequ[grid[current]]
    current = tuple([current[0] + direction[0], current[1] + direction[1]])

vmap = []
with open ('c:/Users/derwin/AOC/22/input', 'r') as f:
    for line in f:
        vmap.append(line)
print("Start")
for row in range(0,len(vmap)):
    for column in range(0,len(vmap)):
                 grid[tuple([column, -1 * row])] = vmap[row][column]

current = tuple([len(vmap)//2, -1 * len(vmap)//2 + 1])

for i in range(0,10000000):
    burst()

printgrid(10)
print(caused)
