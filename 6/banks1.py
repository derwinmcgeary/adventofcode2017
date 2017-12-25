banks = [4,1,	15,	12,	0,	9,	9,	5,	5,	8,	7,	3,	14,	5,	12,	3]
size = len(banks)
maxindex = size -1

print(max(banks))
count = 0
alreadySeen = set(tuple(banks))

while True:
    count = count + 1
    if tuple(banks) == (0, 14, 13, 12, 11, 10, 8, 8, 6, 6, 5, 3, 3, 2, 1, 10):
        print(count)
    toSpread=max(banks)
    currentIndex = banks.index(toSpread)

    banks[currentIndex] = 0

    while toSpread > 0:
        currentIndex = (currentIndex + 1)%size
        banks[currentIndex] = banks[currentIndex] + 1
        toSpread = toSpread - 1
    if tuple(banks) in alreadySeen:
        print(count)
        print(tuple(banks))
        break
    else:
        alreadySeen.add(tuple(banks))
