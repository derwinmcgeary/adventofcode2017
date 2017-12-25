import string
from collections import deque

with open('C:/Users/derwin/AOC/18/input', 'r') as f:
    instructions = f.readlines()
instructions = [x.strip() for x in instructions]

played = 0
current = [0,0]
#    snd X plays a sound with a frequency equal to the value of X.
#    set X Y sets register X to the value of Y.
#    add X Y increases register X by the value of Y.
#    mul X Y sets register X to the result of multiplying the value contained in register X by the value of Y.
#    mod X Y sets register X to the remainder of dividing the value contained in register X by the value of Y (that is, it sets X to the result of X modulo Y).
#    rcv X recovers the frequency of the last sound played, but only when the value of X is not zero. (If it is zero, the command does nothing.)
#    jgz X Y jumps with an offset of the value of Y, but only if the value of X is greater than zero. (An offset of 2 skips the next instruction, an offset of -1 jumps to the previous instruction, and so on.)
class Solo(object):
    def connect(self,other):
        self.outputqueue = other.inputqueue
        
    def snd(self,freq):
        if freq in self.registers:
            freq = self.registers[freq]
        else:
            freq = int(freq)
        self.outputqueue.appendleft(freq)
        self.sent += 1
    
    def Set(self, a,b):
        if b in self.registers:
            self.registers[a] = self.registers[b]
        else:
            self.registers[a] = int(b)
        
    def mul(self,a, b):
        if b in self.registers:
            self.registers[a] *= self.registers[b]
        else:
            self.registers[a] *= int(b)

    def add(self,a, b):
        if b in self.registers:
            self.registers[a] += self.registers[b]
        else:
            self.registers[a] += int(b)

    def mod(self,a, b):
        if b in self.registers:
            self.registers[a] %= self.registers[b]
        else:
            self.registers[a] %= int(b)

    def jgz(self,a, b):
        if b in self.registers:
            b = self.registers[b]
        else:
            b = int(b)
        if a in self.registers:
            a = self.registers[a]
        else:
            a = int(a)
        if a > 0:
            self.current = self.current + b
        else:
 #           print("NOJMP")
            self.current += 1

    def rcv(self,a):
        if len(self.inputqueue) > 0:
            self.registers[a] = self.inputqueue.pop()
            self.waitingfor = '0'
        else:
            self.waitingfor = a
            self.stopped = True

    def __init__(self,idno):
        self.idno = idno
        self.stopped = False
        self.waitingfor = '0'
        self.sent = 0
        self.registers = {}
        for x in string.ascii_lowercase:
            self.registers[x] = 0
        self.registers['p'] = idno
        self.inputqueue = deque()
        self.current = 0
        self.ops = {
            'snd' : self.snd,
            'set' : self.Set,
            'add' : self.add,
            'mul' : self.mul,
            'mod' : self.mod,
            'rcv' : self.rcv,
            'jgz' : self.jgz
        }
        print(self.registers)

    def oneTick(self):
        if self.waitingfor != '0':
            self.rcv(self.waitingfor)
            return
        current = self.current
        if current >=0 and current < len(instructions):
#           print(instructions[current])
            inst = instructions[current].split()
            ins = inst[0]
            if inst[1] in self.registers:
                first = inst[1]
            else:
                first = int(inst[1])
            if len(inst) == 2:
                self.ops[ins](first)
            if len(inst) == 3:
                if inst[2] in self.registers:
                    second = inst[2]
                else:
                    second = int(inst[2])
                self.ops[ins](first,second)
            if ins != 'jgz':
                self.current += 1
            if ins == 'rcv' and self.registers[inst[1]] != 0:
                print(played)
                
thingA = Solo(0)
thingB = Solo(1)

thingA.connect(thingB)
thingB.connect(thingA)

for i in range(0,10000000):
    if thingA.stopped and thingB.stopped:
        stoppedfor += 1
        if stoppedfor > 1000:
            break
    else:
        stoppedfor = 0
    thingB.oneTick()
    thingA.oneTick()

    
