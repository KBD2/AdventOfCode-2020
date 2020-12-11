with open('input.txt', 'r') as inp:
    lines = inp.read().split('\n')

count = 0
x = 0
y = 0

while y < len(lines) - 1:
    x = (x + 3) % len(lines[0])
    y += 1
    if lines[y][x] == '#':
        count += 1

print(count)
