# Solution for the puzzle here: http://adventofcode.com/2017/day/13

with open('C:/Users/derwin/AOC/13/input', 'r') as f:
    input = f.readlines()
input = [x.strip() for x in input]

total = max([int(x.split(': ')[0]) for x in input])
layers = {}
packet = {'depth': -1}
severity = 0

def initialiselayers():
    global input
    for i in input:
        depthRange = i.split(': ')
        depth = depthRange[0]
        Range = int(depthRange[1])
        layers[depth] = {'range': Range, 'current': 0, 'delta': 1}

def makemove(time, delay):
    global severity
    packet['depth'] = time - delay
    ds = str(packet['depth'])
    if ds in layers:
        if getpositionat(layers[ds]['range'],time) == 0:
            severity += packet['depth'] * layers[ds]['range']
            return True
        else:
            return False

def getpositionat(Range,time):
    # get position in the cycle
    if Range == 1:
        return 0
    cycle = (Range - 1)*2
    cyclepos = time % cycle
    if cyclepos < Range:
        return cyclepos
    else:
        return Range - 2 - (cyclepos % Range)

def updateposition(time):
    for layer in layers:
        newpos = getpositionat(layers[layer]['range'], time)
        layers[layer]['current'] = newpos
        
def updatepositions():
#    print(layers)
    for layer in layers:
        if layers[layer]['range'] == 1:
            layers[layer]['delta'] = 0
        newpos = layers[layer]['current'] + layers[layer]['delta']
        if newpos >= 0 and newpos < layers[layer]['range']:
            layers[layer]['current'] = newpos
        else:
            layers[layer]['delta'] = int(layers[layer]['delta'] * -1)
            layers[layer]['current'] += layers[layer]['delta']
        
def dorun(delay):
    global severity
    severity = 0
    global total
    global packet
    caught = 0
#   initialiselayers()
    packet['depth'] = -1
    for i in range(delay,delay + total + 1):
#       updateposition(i)
        if makemove(i, delay):
            caught = caught + 1

    if caught == 0:
        print("Successful attempt at delay: ", delay)
        return True
    else:
#        print("Caught with severity: ", severity)
        return False
def check(delay):
    global severity
    severity = 0
    global total
    caught = 0
    for i in layers:
        if getpositionat(layers[i]['range'], delay + int(i)) == 0:
            caught = 1
            return False

    if caught == 0:
        print("Successful attempt at delay: ", delay)
        return True
    else:
#        print("Caught with severity: ", severity)
        return False

initialiselayers()
import time
t0 = time.time()
print("Starting")
for i in range(0,100000000):
    if check(i):
        break
t1 = time.time()
print("Done! ", t1-t0)
