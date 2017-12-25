with open('C:/Users/derwin/AOC/4/input', 'r') as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content]

validCount = 0
validCountTwo = 0
lines = len(content)
for x in content:
    if len(x.split()) == len(set(x.split())):
        print(x.split())
        validCount = validCount + 1

    x = ' '.join([''.join(sorted(y)) for y in x.split()])
    if len(x.split()) == len(set(x.split())):
        print(x.split())
        validCountTwo = validCountTwo + 1
    

print("Valid out of x lines",validCount, lines)
print("Anagram valid out of x lines", validCountTwo, lines)
