with open('input.txt', 'r') as inp:
    layout = inp.read().split('\n')

rule = {'b': [0], 's': [0, 1, 2, 3, 4]}
    
for count, layer in enumerate(layout):
    layout[count] = list(char for char in layer)

def getHash():
    return hash(tuple(''.join(i) for i in layout))

def countOccupied(x, y):
    deltas = (
        (-1, -1),
        (0, -1),
        (1, -1),
        (1, 0),
        (1, 1),
        (0, 1),
        (-1, 1),
        (-1, 0)
        )
    subtotal = 0
    for checkDelta in deltas:
        checkX = x
        checkY = y
        found = False
        while checkX >= 0 and checkX < len(layout[0]) and checkY >= 0 and checkY < len(layout):
            if not (checkX ^ x | checkY ^ y) or layout[checkY][checkX] == '.':
                checkX += checkDelta[0]
                checkY += checkDelta[1]
            else:
                found = layout[checkY][checkX] == '#'
                break
        if found:
            subtotal += 1
            
    return subtotal

def step(layout):
    new = list([] for i in range(len(layout)))
    for y, row in enumerate(layout):
        for x, space in enumerate(row):
            occupied = countOccupied(x, y)
            if space == 'L' and occupied in rule['b']:
                new[y].append('#')
            elif space == '#' and occupied not in rule['s']:
                new[y].append('L')
            else:
                new[y].append(space)
    return new

def printLayout():
    for row in layout:
        print(''.join(row))

lastHash = 0
while lastHash != getHash():
    lastHash = getHash()
    printLayout()
    print()
    layout = step(layout)

occupied = 0
for row in layout:
    for seat in row:
        if seat == '#':
            occupied += 1
print(occupied)
input()
