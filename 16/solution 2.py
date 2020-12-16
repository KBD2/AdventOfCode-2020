import re

with open('input.txt', 'r') as inp:
    lines = inp.read().split('\n')

def valid(field, poss=-1):
    if poss < 0:
        check = possFields
    else:
        check = [possFields[poss],]
    valid = False
    for item in check:
        item = item[0]
        if (field >= item[0][0] \
            and field <= item[0][1]) \
            or (field >= item[1][0] \
            and field <= item[1][1]):
            valid = True
            break
    return valid

fieldRegex = re.compile("(\d+)-(\d+)")

possFields = []
for c, line in enumerate(lines):
    if line == '':
        lines = lines[c+2:]
        break
    else:
        field = re.findall(fieldRegex, line)
        for i in range(len(field)):
            field[i] = (int(field[i][0]), int(field[i][1]))
        possFields.append((field, line[:line.index(':')]))
        
own = list(map(lambda x: int(x), lines[0].split(',')))
lines = lines[3:]

nearby = []
for line in lines:
    nearby.append(list(map(lambda x: int(x), line.split(','))))

invalid = []

for c, ticket in enumerate(nearby):
    for field in ticket:
        if not valid(field, -1):
            invalid.append(c)

invalid.sort(reverse=True)
for item in invalid:
    del nearby[item]

found = {}
while len(found) < len(possFields):
    for c, poss in enumerate(possFields):
        possible = []
        for part in range(len(own)):
            if part in found.values():
                continue
            match = True
            for item in nearby:
                if not valid(item[part], c):
                    match = False
                    break
            if match:
                possible.append(part)
        if len(possible) == 1:
            found[poss[1]] = possible[0]

total = 1
for item in found:
    if 'departure' in item:
        total *= own[found[item]]

print(total)
