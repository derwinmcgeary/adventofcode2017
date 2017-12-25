import math

target = 347991

shell = 0
bottomrightcorner = 0

for i in range(1,800,2):
    if i**2 > target:
        bottomrightcorner = i**2
        shell = (i-1)/2
        break
# Now that we know which shell
print(shell)

shellsize = shell*2 + 1
print(shellsize)

print(bottomrightcorner)


# Shellsize is always odd

firstinshell = (i-2)*(i-2) + 1 

toprightcorner = firstinshell + shellsize - 2

topleftcorner = toprightcorner  + shellsize - 1

bottomleftcorner = bottomrightcorner - shellsize + 1

print("Target", target)
print("FirstinShell", firstinshell)
print("Shellsize", shellsize)
print("Corners", topleftcorner, toprightcorner, bottomrightcorner, bottomleftcorner)

hdistance = 0
vdistance = 0

if(target >= firstinshell and target <= toprightcorner):
    print("right")
    hdistance = (shellsize - 1)/2
    vdistance = abs(toprightcorner - (shellsize - 1)/2 - target)
if(target > toprightcorner and target <= topleftcorner):
    print("top")
    vdistance = (shellsize - 1)/2
    hdistance = abs(topleftcorner - (shellsize - 1)/2 - target)
if(target > topleftcorner and target <= bottomleftcorner):
    print("left")
    hdistance = (shellsize - 1)/2
    vdistance = abs(bottomleftcorner - (shellsize - 1)/2 - target)
if(target > bottomleftcorner and target <= bottomrightcorner):
    print("bottom")
    vdistance = (shellsize - 1)/2
    hdistance = abs(bottomrightcorner - (shellsize - 1)/2 - target)

print("V,H,total = ", vdistance, hdistance, hdistance + vdistance)


target = 347991

def rotateAntiClockwise(xd,yd):
    # The movement vector rotates through → ↑ ← ↓
    # We implement this as a matrix multiplication
    # [ 0 , -1 ]
    # [ 1 ,  0 ]

    # so we return (0 * xd + -1 * yd) , (1 * xd + 0 * yd) 
    return int(-yd), int(xd)

def canTurnLeft(xpos,ypos,xd,yd):
    xr,yr = rotateAntiClockwise(xd,yd)
    if Matrix[int(xpos + xr)][int(ypos + yr)] == 0:
        return True
    else:
        return False

def sumSurrounding(xpos, ypos):
    summa = Matrix[xpos - 1][ypos + 1] + Matrix[xpos][ypos + 1] + Matrix[xpos + 1][ypos + 1] + Matrix[xpos -1][ypos] + Matrix[xpos + 1][ypos] + Matrix[xpos -1][ypos - 1] + Matrix[xpos][ypos -1] + Matrix[xpos + 1][ypos - 1]
    return summa

print("Now to create an Array!")
# 25*25 should be big enough
w, h = 24, 24;
Matrix = [[0 for x in range(w)] for y in range(h)]

Matrix[int(w/2)][int(h/2)] = 1

# initial position is the middle
xpos=w/2
ypos=h/2
# initial move is left one
xd = 1
yd = 0

for i in range(0,624):
    xpos = int(xpos + xd)
    ypos = int(ypos + yd)
    Matrix[int(xpos)][int(ypos)] = sumSurrounding(int(xpos),int(ypos))
    if canTurnLeft(xpos,ypos,xd,yd):
        xd, yd = rotateAntiClockwise(xd, yd)
    if Matrix[xpos][ypos] > target:
        print(Matrix[xpos][ypos])
        break
    

