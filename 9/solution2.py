with open('input.txt', 'r') as inp:
    lines = inp.read().split('\n')

lines = list(map(lambda x: int(x), lines))

prev = []
line = 0
while line < 25:
    prev.append(lines[line])
    line += 1

while True:
    target = lines[line]
    searchLow = 0
    searchHigh = 1
    found = False
    while searchLow < 24:
        while searchHigh < 25:
            if prev[searchHigh] + prev[searchLow] == target:
                found = True
                break
            searchHigh += 1
        if found:
            break
        searchLow += 1
        searchHigh = searchLow + 1
    if not found:
        invalid = target
        break
    prev.pop(0)
    prev.append(target)
    line += 1

searchLow = 0
searchHigh = 1
weakness = 0
while True:
    lowest = lines[searchLow]
    highest = lines[searchLow]
    while searchHigh < len(lines):
        lowest = min(lowest, lines[searchHigh])
        highest = max(highest, lines[searchHigh])
        if sum(lines[searchLow:searchHigh + 1]) == invalid:
            weakness = lowest + highest
            break
        searchHigh += 1
    if weakness > 0:
        break
    searchLow += 1
    searchHigh = searchLow + 1
print(weakness)
