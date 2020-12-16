import re

with open('input.txt', 'r') as inp:
    lines = inp.read().split('\n')

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
        possFields.append(field)
        
own = list(map(lambda x: int(x), lines[0].split(',')))
lines = lines[3:]

nearby = []
for line in lines:
    nearby.append(list(map(lambda x: int(x), line.split(','))))

errorRate = 0

for ticket in nearby:
    for field in ticket:
        valid = False
        for item in possFields:
            if field >= item[0][0] \
               and field <= item[0][1] \
               or field >= item[1][0] \
               and field <= item[1][1]:
                valid = True
                break
        if not valid:
            errorRate += field

print(errorRate)
