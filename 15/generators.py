class Generator:
    def __init__(self, factor, seed, multiple=1):
        self.factor = factor
        self.current = seed
        self.divisor = 2147483647
        self.multiple = multiple

    def getNext(self):
        self.current =  ( self.current * self.factor ) % self.divisor        
        while self.current % self.multiple != 0:
            self.current = ( self.current * self.factor ) % self.divisor
        return self.current

def judge(a,b, mask):
    return a & mask == b & mask


mask = 0b1111111111111111
limit = 5000000
factora = 16807
factorb = 48271
seeda = 679
seedb =  771
#seeda = 65
#seedb = 8921
multiplea = 4
multipleb = 8
gena = Generator(factora,seeda, multiplea)
genb = Generator(factorb,seedb, multipleb)
total = 0

import time
ta = time.time()
for i in range(0,limit):
    if judge(gena.getNext(),genb.getNext(), mask):
        total += 1
tb = time.time()

print("Got X matches in Y seconds", total, tb - ta)
