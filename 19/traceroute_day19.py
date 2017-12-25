routemap = []
with open ('c:/Users/derwin/AOC/19/input', 'r') as f:
    for line in f:
        routemap.append(line)
print("Start")
for row in routemap:
    print(row)


class Tracer(object):
    def __init__(self, routemap):
        self.routemap = routemap
        self.xpos = routemap[0].find('|')
        self.ypos = 0
        self.xd = 0
        self.yd =1
        self.fitbit = 1 # we just made the first step
        self.distances = {}
        self.encountered = []

    def get(self):
        return self.xpos, self.ypos, self.routemap[self.ypos][self.xpos]

    def move(self):
        lastseen = self.routemap[self.ypos][self.xpos]
        self.xpos = self.xpos + self.xd
        self.ypos = self.ypos + self.yd
        self.fitbit += 1
        latestseen = self.routemap[self.ypos][self.xpos]
        if latestseen in string.ascii_uppercase:
            self.distances[latestseen] = self.fitbit
        if latestseen in '+-|':
            self.control(lastseen,latestseen)
        else:
            self.encountered.append(latestseen)
            self.control(lastseen,latestseen)

    def turn(self):
        directions = {
            'left'  : lambda dx,dy: [dy, -dx],
            'right' : lambda dx, dy: [-dy, dx]
        }
        found = False
        for i in ['left','right']:
            if self.look(i):
                self.xd, self.yd = directions[i](self.xd,self.yd)
                found = True
        if found == False:
            print("EOTL")
            
    def look(self,direction):
        directions = {
            'left'  : lambda dx,dy: [dy, -dx],
            'right' : lambda dx, dy: [-dy, dx]
        }
        ok = False
        nx,ny = directions[direction](self.xd,self.yd)
        if self.xpos + nx >= 0 and self.xpos + nx < len(self.routemap[self.ypos]):
            if self.ypos + ny >= 0 and self.ypos + ny < len(self.routemap):
                if self.routemap[self.ypos + ny][self.xpos + nx] != ' ':
                    ok = True
        return ok
        
    def control(self,last,current):
        # set new xd and yd based on the previous input, current input, and map layout
#        print(last,current)
        if last == current:
            return
        if current == '+': # corner
            self.turn()

counter = 1
tracer = Tracer(routemap)
for i in range(0,500000):
#    print(tracer.get())
    counter += 1
    tracer.move()
    if 'S' in tracer.encountered:
        print(counter)
        break

print(''.join(tracer.encountered[:tracer.encountered.index(' ')]))
print(tracer.distances)
