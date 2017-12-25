
maze = []

with open('C:/Users/derwin/AOC/5/input', 'r') as f:
    for line in f:
       maze.append(int(line))
print(maze)
position = 0
end=len(maze)
i = 0

while True:
    i = i + 1
    newposition = position + maze[position]
    if maze[position] > 2:
        shift = -1
    else:
        shift = 1
    maze[position] = maze[position] + shift
    position = newposition
    if position < 0 or position >= end:
        print(i)
        break
