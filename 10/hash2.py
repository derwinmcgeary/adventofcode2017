class Loop(object):
    contents = []
    size = 0

    def __init__(self, size):
        self.contents = list(range(0,size))
        self.size = size

    def get(self):
        return self.contents

    # Move the whole ring so our start position is zero
    def rotate(self, offset):
        offset = offset % self.size
        if offset < 0:
            offset = self.size - offset
        firsthalf = self.contents[offset:]
        secondhalf = self.contents[:offset]
        self.contents = firsthalf + secondhalf
        return self.contents
        

    def simpleReverse(self,start, length):
        rotato = self.rotate(start)
        selection = rotato[:length]
        rev = selection[::-1]
        self.contents[:length] = rev
        self.contents = self.rotate(-1 * start)

class Hasher(object):

    def __init__(self, listLength, blocksize, rounds):
        self.listLength = listLength
        self.blocksize = blocksize
        self.rounds = rounds

    def densifyBlock(self, block):
        result = 0
        for x in block:
            result ^= x
        return result

    def hashed(self, salted):
        rope = Loop(self.listLength)
        position = 0
        skip = 0
        for i in range(0,self.rounds):
            for j in salted:
                rope.simpleReverse(position,j)
                position = (position + j + skip) % listLength
                skip = skip + 1
        return rope.get()

    def densify(self, sparseHash):
        denseHash = ''
        for i in range(0,self.listLength//self.blocksize):
            output = self.densifyBlock(sparseHash[i * self.blocksize:i*self.blocksize + self.blocksize])
            denseHash = denseHash + format(output,'02x')
        return denseHash

    def salted(self,input):
        # Convert from a string to a list of numbers with salt
        suffix = [17, 31, 73, 47, 23]
        return [int(ord(x)) for x in input] + suffix


    def createHash(self,instring):
        salty = self.salted(instring)

        sparseHash = self.hashed(salty)
        denseHash = self.densify(hashed(salty))
        return denseHash


#Here are some example hashes:

#    The empty string becomes a2582a3a0e66e6e86e3812dcb672a272.
#    AoC 2017 becomes 33efeb34ea91902bb2f59c9920caa6cd.
#    1,2,3 becomes 3efbe78a8d82f29979031a4aa0b16a9d.
#    1,2,4 becomes 63960835bcdc130f0b66d7ff4f6a5a8e.
#
# Stored as a dictionary below
tests = {'' : 'a2582a3a0e66e6e86e3812dcb672a272', 'AoC 2017' : '33efeb34ea91902bb2f59c9920caa6cd', '1,2,3' : '3efbe78a8d82f29979031a4aa0b16a9d','1,2,4' : '63960835bcdc130f0b66d7ff4f6a5a8e'}


# Initialising our Hasher
listLength = 256
rounds = 64
blocksize = 16

# Answer to Part One
# Unit tests
testsOne = {tuple([3,4,1,5]):12}
hasherTest = Hasher(5,blocksize,1) # one round with 5 elements
for x in testsOne:
    result = hasherTest.hashed(list(x))
    if result[0]*result[1] != testsOne[x]:
        print("Test Failed!")


hasherOne = Hasher(listLength, blocksize, 1)
partOneInput = [94,84,0,79,2,27,81,1,123,93,218,23,103,255,254,243]
answers = hasherOne.hashed(partOneInput)
print("Answer to part one is", answers[0]*answers[1])

# Answer to Part Two
hasher = Hasher(listLength, blocksize, rounds)

# Unit tests
tested = 0
correct = 0
for i in tests:
    tested += 1
    if hasher.createHash(i) == tests[i]:
        correct += 1
    else:
        print(hasher.createHash(i))



input = '94,84,0,79,2,27,81,1,123,93,218,23,103,255,254,243'
if correct == tested:
    print("Hash of", input, "is", hasher.createHash(input))
else:
    print(correct, "out of", tested, "tests passed")
