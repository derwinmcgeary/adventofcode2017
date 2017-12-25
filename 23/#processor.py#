import string
import time
from collections import deque

with open('C:/Users/derwin/AOC/23/input', 'r') as f:
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
        self.multcount += 1

    def add(self,a, b):
        if b in self.registers:
            self.registers[a] += self.registers[b]
        else:
            self.registers[a] += int(b)

    def sub(self,a, b):
        if b in self.registers:
            self.registers[a] -= self.registers[b]
        else:
            self.registers[a] -= int(b)

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
    def jnz(self,a, b):
        if b in self.registers:
            b = self.registers[b]
        else:
            b = int(b)
        if a in self.registers:
            a = self.registers[a]
        else:
            a = int(a)
        if a != 0:
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
        self.multcount = 0
        self.idno = idno
        self.stopped = False
        self.waitingfor = '0'
        self.sent = 0
        self.registers = {}
        for x in 'abcdefgh':
            self.registers[x] = 0
        self.registers = {'a': 1, 'b': 125400, 'c': 125400, 'd': 125400, 'e': 125400, 'f': 1, 'g': 0, 'h': 500}
        self.inputqueue = deque()
        self.current = 20
        self.ops = {
            #'snd' : self.snd,
            'set' : self.Set,
            #'add' : self.add,
            'mul' : self.mul,
            #'mod' : self.mod,
            #'rcv' : self.rcv,
            'jnz' : self.jnz,
            #'jgz' : self.jgz
            'sub' : self.sub
        }
        print(self.registers)
    def getreg(self,x):
        if x in self.registers:
            return self.registers[x]
        else:
            return int(x)
    def oneTick(self):
        if self.waitingfor != '0':
            self.rcv(self.waitingfor)
            return
        current = self.current
        if current >=0 and current < len(instructions):
            inst = instructions[current].split()
            ins = inst[0]
            if current == 11:
                print(self.registers)
            print(current, ':', instructions[current],':', self.getreg(inst[1]), self.getreg(inst[2]))
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
            if ins != 'jnz':
                self.current += 1
            if ins == 'rcv' and self.registers[inst[1]] != 0:
                print(played)
            return True
        else:
            return False


procOne = Solo(0)
mc = 0
while procOne.oneTick():
    if procOne.registers['h'] != mc:
        mc = procOne.registers['h']
        print(mc)

print(procOne.registers['h'])
