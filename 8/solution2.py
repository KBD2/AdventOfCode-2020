import re

with open('input.txt', 'r') as inp:
    lines = inp.read().split('\n')

instructionRegex = re.compile("(jmp|acc|nop) ((?:\+|\-)[0-9]+)")

def execute():
    pc = 0
    acc = 0
    executed = set()
    while pc not in executed:
        if pc == len(lines):
            return acc
        executed.add(pc)
        instruction = re.match(instructionRegex, lines[pc]).groups()
        if instruction[0] == 'acc':
            acc += int(instruction[1])
            pc += 1
        elif instruction[0] == 'jmp':
            pc += int(instruction[1])
        elif instruction[0] == 'nop':
            pc += 1
    return -1

linesCopy = lines.copy()
lastLine = -1
while True:
    lines = linesCopy.copy()
    lastLine += 1
    while re.match(instructionRegex, lines[lastLine]).groups()[0] == 'acc':
        lastLine += 1
    instruction = re.match(instructionRegex, lines[lastLine]).groups()
    if instruction[0] == 'jmp':
        lines[lastLine] = 'nop +0'
    else:
        lines[lastLine] = 'jmp ' + instruction[1]
    res = execute()
    if res > -1:
        print(res)
        break
