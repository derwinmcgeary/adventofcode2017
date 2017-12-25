filename = 'C:/Users/derwin/AOC/25/input'
#filename = 'C:/Users/derwin/AOC/25/testinput' 

with open(filename, 'r') as f:
    instructions = f.readlines()
instructions = [x.strip().split() for x in instructions]

states = {}
currentstate = ''
createstate = ''
createif = ''
cursor = 0
totalsteps = 0
tape = {'0': 0}
dirs = {'left' : -1, 'right' : 1}
for x in instructions:
    print(x)
    if len(x) == 0:
        continue
    if x[0] == 'Begin':
        currentstate = x[3][0]
    if x[0] == 'Perform':
        totalsteps = int(x[5])
    if x[0] == 'In':
        createstate = x[2][0]
        states[createstate] = {}
    if x[0] == 'If':
        createif = x[-1][0]
        states[createstate][createif] = {}
    if x[0] == '-':
        if x[1] == 'Write':
            states[createstate][createif][x[1]] = int(x[4][0])
        if x[1] == 'Move':
            states[createstate][createif][x[1]] = dirs[x[6][:-1]]
        if x[1] == 'Continue':
            states[createstate][createif][x[1]] = x[-1][0]
print(states)


def dostep():
    global tape
    global cursor
    global states
    global currentstate
    
    curval = tape[str(cursor)]
    #print("State is {}, under tape value is {}".format(currentstate,curval))
    steps = states[currentstate][str(curval)]
    #print(steps)
    tape[str(cursor)] = steps['Write']
    #print(tape[str(cursor)])
    cursor = cursor + steps['Move']
    #print(steps['Move'], cursor)
    extendtapeifnecessary(cursor)
    currentstate = steps['Continue']

    #print(currentstate,cursor,tape[str(cursor)])

def extendtapeifnecessary(position):
    if str(position) not in tape:
        tape[str(position)] = 0

for i in range(0, totalsteps):
    dostep()
totaliser = 0
for z in tape:
    totaliser += tape[z]

print(totaliser)
