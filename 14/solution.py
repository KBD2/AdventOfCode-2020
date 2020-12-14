import re

with open('input.txt', 'r') as inp:
    instructions = inp.read().split('\n')

memRegex = re.compile("mem\[(\d*)\] = (\d*)")
mask = ''
memory = {}

for inst in instructions:
    if inst[:4] == 'mask':
        mask = inst[7:]
    else:
        parts = re.match(memRegex, inst).groups()
        value = int(parts[1])
        for idx, bit in enumerate(mask):
            if bit == '1':
                value |= 1 << (35 - idx)
            elif bit == '0':
                value &= ~(1 << (35 - idx))
        memory[int(parts[0])] = value

print(sum(memory.values()))
