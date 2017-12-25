# Solution for the puzzle here: http://adventofcode.com/2017/day/12

with open('C:/Users/derwin/AOC/12/input', 'r') as f:
    progs = f.readlines()
progs = [x.strip() for x in progs]
groups = {}
for x in progs:
    groups[x.split(' <-> ')[0]] = set(z.strip() for z in x.split(' <-> ')[1].split(',')) 

# I feel like this gets too nested, but it works
changeFlag = True
while changeFlag == True:
    changeFlag = False
    for x in groups:
        for y in groups[x]: # It's pronounced "group sex"
            for z in groups[y]:
                if z not in groups[x]:
                    groups[x] = groups[x] | groups[y]
                    changeFlag = True

count = 0
for x in groups:
    if x in groups['0']:
        count += 1

print("Count is ", count)

groupset = set()

for x in groups:
    groupset = groupset | {','.join(sorted(list(groups[x])))}

print("Number of groups is ", len(groupset))

