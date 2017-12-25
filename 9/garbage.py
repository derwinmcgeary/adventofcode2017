with open('C:/Users/derwin/AOC/9/input', 'r') as f:
    content = f.readlines()
content = [x.strip() for x in content]

content = ''.join(content)

# content = '{{<ab>},{<ab>},{<ab>},{<ab>}}'
# content = '{{<a!>},{<a!>},{<a!>},{<ab>}}'
# content = '{{<!!>},{<!!>},{<!!>},{<!!>}}'
inJunk = False
skipping = False
score = 0
level = 0
garbageChar = 0


def levelup():
    global score
    global level
    level = level + 1
    score = score + level

def leveldown():
    global level
    level = level - 1

def startjunk():
    global inJunk
    inJunk = True
    

def endjunk():
    global inJunk
    inJunk = False

def skipnext():
    global skipping
    skipping = True

ops = {
    '{': levelup,
    '}': leveldown,
    '<': startjunk,
    '>': endjunk,
    '!': skipnext
}


for i in content:
    print(i)
    if skipping == False:
        if inJunk == True:
            if i not in '>!':
                garbageChar = garbageChar + 1
        if i in ops and (inJunk == False or i in '>!'):
            ops[i]()
    else:
        skipping = False

print("Final score is ", score)
print("Garbage chars = ", garbageChar)
