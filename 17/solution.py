with open('input.txt', 'r') as inp:
    rows = inp.read().split('\n')
    
class Cube:
    def __init__(self, active, x, y, z):
        self.active = active
        self.x = x
        self.y = y
        self.z = z

def computeHash(x, y, z):
    return (x, y, z)

def compute(cubeMap, x, y, z):
    total = 0
    for cZ in range(z - 1, z + 2):
        for cY in range(y - 1, y + 2):
            for cX in range(x - 1, x + 2):
                if not (cZ ^ z or cY ^ y or cX ^ x):
                    continue
                check = computeHash(cX, cY, cZ)
                if check not in cubeMap or not cubeMap[check].active:
                    continue
                else:
                    total += 1
    return total

def iterate(cubeMap):
    rule = {'b': [3], 's': [2, 3]}
    new = {}
    ignored = []
    for cube in cubeMap.values():
        for cZ in range(cube.z - 1, cube.z + 2):
            for cY in range(cube.y - 1, cube.y + 2):
                for cX in range(cube.x - 1, cube.x + 2):
                    cubeHash = computeHash(cX, cY, cZ)
                    if cubeHash in new or cubeHash in ignored:
                        continue
                    neighbours = compute(cubeMap, cX, cY, cZ)
                    if cubeHash not in cubeMap:
                        if neighbours in rule['b']:
                            new[cubeHash] = Cube(True, cX, cY, cZ)
                        else:
                            ignored.append(cubeHash)
                    else:
                        if cubeMap[cubeHash].active and neighbours not in rule['s']:
                            new[cubeHash] = Cube(False, cX, cY, cZ)
                        elif not cubeMap[cubeHash].active and neighbours in rule['b']:
                            new[cubeHash] = Cube(True, cX, cY, cZ)
                        else:
                            new[cubeHash] = cubeMap[cubeHash]
    return new

def output(cubeMap):
    xBounds = [0, 0]
    yBounds = [0, 0]
    zBounds = [0, 0]

    for cube in cubeMap.values():
        xBounds[0] = min(xBounds[0], cube.x)
        xBounds[1] = max(xBounds[1], cube.x)
        yBounds[0] = min(yBounds[0], cube.y)
        yBounds[1] = max(yBounds[1], cube.y)
        zBounds[0] = min(zBounds[0], cube.z)
        zBounds[1] = max(zBounds[1], cube.z)

    for z in range(zBounds[0], zBounds[1] + 1):
        rows = []
        for y in range(yBounds[0], yBounds[1] + 1):
            column = ''
            for x in range(xBounds[0], xBounds[1] + 1):
                check = computeHash(x, y, z)
                if check not in cubeMap or not cubeMap[check].active:
                    column = column + '.'
                else:
                    column = column + '#'
            rows.append(column)
        for row in rows:
            print(row)
        print()

cubeMap = {}

for y, row in enumerate(rows):
    for x, char in enumerate(row):
        cubeMap[computeHash(x, y, 0)] = Cube(char == '#', x, y, 0)

output(cubeMap)
for i in range(6):
    print(f"Iteration {i + 1}")
    cubeMap = iterate(cubeMap)
    output(cubeMap)

active = 0
for cube in cubeMap.values():
    if cube.active:
        active += 1

print(active)
