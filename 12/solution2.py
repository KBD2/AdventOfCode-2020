with open('input.txt', 'r') as inp:
    directions = inp.read().split('\n')

x = 0
y = 0
wX = 10
wY = 1

for direction in directions:
    instruction = direction[0]
    amount = int(direction[1:])
    if instruction == 'N':
        wY += amount
    elif instruction == 'S':
        wY -= amount
    elif instruction == 'E':
        wX += amount
    elif instruction == 'W':
        wX -= amount
    elif instruction == 'R':
        for i in range(amount // 90):
            if wX >= 0 and wY >= 0:
                wX, wY = wY, -wX
            elif wX >= 0 and wY < 0:
                wX, wY = wY, -wX
            elif wX < 0 and wY < 0:
                wX, wY = wY, -wX
            elif wX < 0 and wY >= 0:
                wX, wY = wY, -wX
    elif instruction == 'L':
        for i in range(amount // 90):
            if wX >= 0 and wY >= 0:
                wX, wY = -wY, wX
            elif wX >= 0 and wY < 0:
                wX, wY = -wY, wX
            elif wX < 0 and wY < 0:
                wX, wY = -wY, wX
            elif wX < 0 and wY >= 0:
                wX, wY = -wY, wX
    elif instruction == 'F':
        for i in range(amount):
            x += wX
            y += wY

print(abs(x) + abs(y))
    
