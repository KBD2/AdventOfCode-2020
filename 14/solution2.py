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
        index = int(parts[0])
        value = int(parts[1])
        floating = []
        for idx, bit in enumerate(mask):
            if bit == '1':
                index |= 1 << (35 - idx)
            elif bit == 'X':
                floating.append(35 - idx)
        for i in range(2 ** len(floating)):
            for c, idx in enumerate(floating):
                if i & (1 << c) > 0:
                    index |= 1 << idx
                else:
                    index &= ~(1 << idx)
            memory[index] = value

print(sum(memory.values()))
