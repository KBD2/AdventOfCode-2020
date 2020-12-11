import re

with open('input.txt', 'r') as inp:
    lines = inp.read().split('\n')

topRegex = re.compile("^(\w* \w*)")
subRegex = re.compile("[0-9] (\w* \w*)")

bags = {}

def addBag(line):
    top = re.search(topRegex, line).groups()[0]
    inside = re.findall(subRegex, line)
    bags[top] = False
    if not inside:
        return
    for match in inside:
        if match == "shiny gold":
            bags[top] = True
            return
        if match not in bags:
            for line in lines:
                if re.search(topRegex, line).groups()[0] == match:
                    addBag(line)
                    break
        if bags[match]:
            bags[top] = True
            return

for line in lines:
    if re.search(topRegex, line).groups()[0] not in bags:
        addBag(line)

total = 0
for bag in bags:
    if bags[bag]:
        total += 1

print(total)
