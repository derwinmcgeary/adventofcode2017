with open('C:/Users/derwin/AOC/8/input', 'r') as f:
    content = f.readlines()
content = [x.strip() for x in content]

register = {}
maxval = 0

# Let's define our operations and put the functions (first-class variables!) in a dict

ops = {
    '==': lambda a,b: a == b,
    '!=': lambda a,b: a != b,
    '>': lambda a,b: a > b,
    '<': lambda a,b: a < b,
    '>=': lambda a,b: a >=b,
    '<=': lambda a,b: a <= b,
    'inc': lambda a,b: a+b,
    'dec': lambda a,b: a-b
}

# convenience function for lazy assignment/comparison
def registrate(reg):
    if reg not in register:
        register[reg] = 0
    return reg


# Those functions make evaluate() much neater, since it just has to break down the expression and pass to the dict of functions
def evaluate(condition):
    clause = condition.split()
    reg = registrate(clause[0])
    conditional = clause[1]
    value = int(clause[2])
    return ops[conditional](register[reg], value)

# I added inc and dec to ops{} so that I could simplify follow()
def follow(instruction):
    clause = instruction.split()
    reg = registrate(clause[0])
    opcode = clause[1]
    value = int(clause[2])

    newval = ops[opcode](register[reg], value) # this looks up the dictionary and add/subtracts as needed: if we add ops, we can leave this code as-is
    register[reg] = newval
    updateMax(newval)

def getMax(register):
    maximum = max(register, key=register.get)
    return maximum, register[maximum]

def updateMax(value):
    global maxval
    maxval = max(value,maxval)

# All functions in place, we parse the instructions
for x in content:
    clause = x.split(' if ')
    instruction = clause[0]
    condition = clause[1]

    if evaluate(condition):
        follow(instruction)

print("Maximum register is ", getMax(register))
print("Maximum ever was ", maxval)
