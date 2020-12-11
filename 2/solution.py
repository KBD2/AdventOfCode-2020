import re

regex = re.compile(r"([0-9]{1,2})\-([0-9]{1,2}) ([a-z]{1}): (\S*)")

with open('input.txt', 'r') as inp:
    lines = inp.read().split('\n')

count = 0
for line in lines:
    groups = re.match(regex, line)
    if not groups:
        print("Error: Regex didn't match!")
        continue
    first = int(groups[1]) - 1
    second = int(groups[2]) - 1
    letter = groups[3]
    password = groups[4]

    contains = (password[first] == letter) ^ (password[second] == letter)
    if contains:
        count += 1

print(count)
