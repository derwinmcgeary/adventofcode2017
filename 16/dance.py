import string
class Dancers(object):
    contents = []
    size = 0

    def __init__(self, size):
        self.contents = list(string.ascii_lowercase)[0:size]
        self.size = size

    def get(self):
        return ''.join(self.contents)

    # Move the whole ring so our start position is zero
    def spin(self, offset):
        offset = -1 * offset % self.size
        if offset < 0:
            offset = self.size - offset
        firsthalf = self.contents[offset:]
        secondhalf = self.contents[:offset]
        self.contents = firsthalf + secondhalf
        return self.contents
        
    def exchange(self,a,b):
        tmp = self.contents[a]
        self.contents[a] = self.contents[b]
        self.contents[b] = tmp
        
    def swap(self, a, b):
        self.exchange(self.get().find(a),self.get().find(b))
        
    def parseInstruction(self,call):
        instruction = call[0]
        target = call[1:]
        if instruction == 's':
            self.spin(int(target))
            return
        targets = target.split('/')        
        if instruction == 'x':
            self.exchange(int(targets[0]),int(targets[1]))
            return
        if instruction == 'p':
            self.swap(targets[0],targets[1])
            return
            
    def simpleReverse(self,start, length):
        rotato = self.spin(start)
        selection = rotato[:length]
        rev = selection[::-1]
        self.contents[:length] = rev
        self.contents = self.spin(-1 * start)

# Load input
#For example, with only five programs standing in a line (abcde), they could do the following dance:

#    s1, a spin of size 1: eabcd.
#    x3/4, swapping the last two programs: eabdc.
#    pe/b, swapping programs e and b: baedc.

#After finishing their dance, the programs end up in order baedc.
dancers = Dancers(5)
answer = 'baedc'
for i in 's1,x3/4,pe/b'.split(','):
    dancers.parseInstruction(i)
if dancers.get() == answer:
    print("Test successful!")
