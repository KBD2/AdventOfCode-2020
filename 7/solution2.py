import re

with open('input.txt', 'r') as inp:
    lines = inp.read().split('\n')

topRegex = re.compile("^(\w* \w*)")
subRegex = re.compile("([0-9]) (\w* \w*)")

bags = {}
total = 0

def findBag(line):
    sub = re.findall(subRegex, line)
    subtotal = 1
    if len(sub) == 0:
        return subtotal
    for bag in sub:
        for line in lines:
            if re.search(topRegex, line).groups()[0] == bag[1]:
                subtotal += int(bag[0]) * findBag(line)
    return subtotal

for line in lines:
    if re.search(topRegex, line).groups()[0] == "shiny gold":
        print(findBag(line) - 1)
        break
