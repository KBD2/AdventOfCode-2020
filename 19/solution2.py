import re

with open('input.txt', 'r') as inp:
    lines = inp.read().split('\n')

partsRegex = re.compile("(?:a|b)|\||\d+")

rulesRaw = {}
rules = {}

def compileRule(rule, depth):
    if depth == 10:
        return ''
    final = ""
    raw = rulesRaw[rule]
    parts = re.findall(partsRegex, raw)
    for part in parts:
        if part[0] in "0123456789":
            num = int(part)
            if num == rule:
                final += '(' + compileRule(num, depth + 1) + ')'
            elif num in rules:
                final += '(' + rules[num] + ')'
            else:
                final += '(' + compileRule(num, 0) + ')'
        else:
            final += part
    
    rules[rule] = final
    return final

for idx, line in enumerate(lines):
    if line == '':
        lines = lines[idx+1:]
        break
    start = line.index(':')
    if 'a' in line or 'b' in line:
        rulesRaw[int(line[:start])] = 'a' if 'a' in line else 'b'
    else:
        rulesRaw[int(line[:start])] = line[start+2:]

rule = re.compile("^" + compileRule(0, 0) + "$")

total = 0
for line in lines:
    if re.match(rule, line):
        total += 1
print(total)
