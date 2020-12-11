import re

with open('input.txt', 'r') as inp:
    lines = inp.read().split('\n')

instructionRegex = re.compile("(jmp|acc|nop) ((?:\+|\-)[0-9]+)")

pc = 0
acc = 0
executed = set()
while pc not in executed:
    executed.add(pc)
    instruction = re.match(instructionRegex, lines[pc]).groups()
    if instruction[0] == 'acc':
        acc += int(instruction[1])
        pc += 1
    elif instruction[0] == 'jmp':
        pc += int(instruction[1])
    elif instruction[0] == 'nop':
        pc += 1

print(acc)
