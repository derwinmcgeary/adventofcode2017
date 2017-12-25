class Loop(object):
    contents = []
    size = 0

    def __init__(self, size):
        self.contents = list(range(0,size))
        self.size = size

    def get(self):
        return self.contents

# Move the whole ring so our start position is zero
    def leftshift(self, offset):
        offset = offset % self.size
        print("shift ", self.contents, " left by ", offset)
        firsthalf = self.contents[offset:]
        secondhalf = self.contents[:offset]
        print("result ", firsthalf + secondhalf)
        return firsthalf + secondhalf


    def rightshift(self, offset, ring):
        offset = offset % self.size
        print("Shift ", ring, " right by ", offset)
        firsthalf = ring[-offset:]
        secondhalf = ring[:-offset]
        print("First half : ", firsthalf, " Second Half: ", secondhalf)
        print("Result: ", firsthalf + secondhalf)
        return firsthalf + secondhalf
        
        rev = reversed(self.contents[start:end])
        self.contents[start:end] = rev
        print(self.contents[-2:2])

    def reverse(self, start, length):
#        print("Starting reverse with ",self.contents)
#        print("Start and Requested end on ring of size", start, start + length, self.size)
        normalisedEnd = (start + length) % self.size
        if normalisedEnd <= start: # i.e. we overshoot the end
            print("Selection: ", self.contents[:normalisedEnd], ')', self.contents[normalisedEnd:start], '(', self.contents[start:])
            secondhalf = self.contents[:normalisedEnd]
#            print("Second Half, Start, End ", secondhalf, start, normalisedEnd)
            selection = self.contents[start:]
#            print("First Half ",selection)
            selection.extend(secondhalf)
            rev = selection[::-1]
            print("Selected and Reversed", selection,rev)
            for i in range(0,len(rev)):
                self.contents[(start + i) % self.size] = rev[i]
            
        else:
            selection = self.contents[start:normalisedEnd]
            print("Selection: ", self.contents[:start], '(', selection, ')', self.contents[normalisedEnd:])
            rev = selection[::-1]
            self.contents[start:normalisedEnd] = rev
        print("Ending reverse with", self.contents)

    def simpleReverse(self,start, length):
        rotato = self.leftshift(start)
        selection = rotato[:length]
        rev = selection[::-1]
        rotato[:length] = rev
        self.contents = self.rightshift(start,rotato)
        
        
input = [94,84,0,79,2,27,81,1,123,93,218,23,103,255,254,243]
listLength = 256
skip = 0
position = 0



#Here are some example hashes:

#    The empty string becomes a2582a3a0e66e6e86e3812dcb672a272.
#    AoC 2017 becomes 33efeb34ea91902bb2f59c9920caa6cd.
#    1,2,3 becomes 3efbe78a8d82f29979031a4aa0b16a9d.
#    1,2,4 becomes 63960835bcdc130f0b66d7ff4f6a5a8e.

#input = ''
#listLength = 256


rope = Loop(listLength)

for i in input:
    print("Skip ", skip)
    rope.simpleReverse(position,i)
    position = (position + i + skip) % listLength
    skip = skip + 1

