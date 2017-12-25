with open('C:/Users/derwin/AOC/11/input', 'r') as f:
    path = f.readlines()
path = [x.strip() for x in path]

path = ''.join(path).split(',')

# Using Cubic Coordinates (sliced-through cubes are hexagons!) from https://www.redblobgames.com/grids/hexagons/

position = {'x':0,'y':0,'z':0} # Start at 0,0,0

direction = {
    'n' : {'x':0,'y':1,'z':-1},
    's' : {'x':0,'y':-1,'z':1},
    'ne' : {'x':1,'y':0,'z':-1},
    'se' : {'x':1,'y':-1,'z':0},
    'nw' : {'x':-1,'y':1,'z':0},
    'sw' : {'x':-1,'y':0,'z':1}
}

def move(dir):
    for i in position: position[i] += direction[dir][i]

def distance(pos):
    return (abs(pos['x']) + abs(pos['y']) + abs(pos['z']))//2

maxdist = 0

for step in path:
    move(step)
    maxdist = max(maxdist,distance(position))

print(distance(position))
print(maxdist)

