with open('input.txt', 'r') as inp:
    directions = inp.read().split('\n')
    
heading = 90
x = 0
y = 0

for direction in directions:
    instruction = direction[0]
    amount = int(direction[1:])
    if instruction == 'N':
        y += amount
    elif instruction == 'S':
        y -= amount
    elif instruction == 'E':
        x += amount
    elif instruction == 'W':
        x -= amount
    elif instruction == 'R':
        heading += amount
    elif instruction == 'L':
        heading -= amount
    elif instruction == 'F':
        if heading == 0:
            y += amount
        elif heading == 90:
            x += amount
        elif heading == 180:
            y -= amount
        elif heading == 270:
            x -= amount
    heading %= 360

print(abs(x) + abs(y))
    
