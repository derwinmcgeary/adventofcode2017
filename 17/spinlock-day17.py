from collections import deque

input = 343
endvalue = 50000000
buffer = deque([0])
for i in range(1,endvalue + 1):
    buffer.rotate(-input)
    buffer.append(i)
print(buffer[buffer.index(0) + 1])
