with open('input.txt', 'r') as inp:
    rows = inp.read().split('\n')
    
class Cube:
    def __init__(self, active, x, y, z, w):
        self.active = active
        self.x = x
        self.y = y
        self.z = z
        self.w = w

def computeHash(x, y, z, w):
    return (x, y, z, w)

def compute(cubeMap, x, y, z, w):
    total = 0
    for cW in range(w - 1, w + 2):
        for cZ in range(z - 1, z + 2):
            for cY in range(y - 1, y + 2):
                for cX in range(x - 1, x + 2):
                    if not (cW ^ w or cZ ^ z or cY ^ y or cX ^ x):
                        continue
                    check = computeHash(cX, cY, cZ, cW)
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
        for cW in range(cube.w - 1, cube.w + 2):
            for cZ in range(cube.z - 1, cube.z + 2):
                for cY in range(cube.y - 1, cube.y + 2):
                    for cX in range(cube.x - 1, cube.x + 2):
                        cubeHash = computeHash(cX, cY, cZ, cW)
                        if cubeHash in new or cubeHash in ignored:
                            continue
                        neighbours = compute(cubeMap, cX, cY, cZ, cW)
                        if cubeHash not in cubeMap:
                            if neighbours in rule['b']:
                                new[cubeHash] = Cube(True, cX, cY, cZ, cW)
                            else:
                                ignored.append(cubeHash)
                        else:
                            if cubeMap[cubeHash].active and neighbours not in rule['s']:
                                new[cubeHash] = Cube(False, cX, cY, cZ, cW)
                            elif not cubeMap[cubeHash].active and neighbours in rule['b']:
                                new[cubeHash] = Cube(True, cX, cY, cZ, cW)
                            else:
                                new[cubeHash] = cubeMap[cubeHash]
    return new

cubeMap = {}

for y, row in enumerate(rows):
    for x, char in enumerate(row):
        cubeMap[computeHash(x, y, 0, 0)] = Cube(char == '#', x, y, 0, 0)

for i in range(6):
    print(f"Iteration {i + 1}")
    cubeMap = iterate(cubeMap)

active = 0
for cube in cubeMap.values():
    if cube.active:
        active += 1

print(active)
