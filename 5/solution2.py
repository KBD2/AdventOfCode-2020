with open('input.txt', 'r') as inp:
    lines = inp.read().split('\n')

seats = []
for line in lines:
    bottom = 0
    top = 127
    for inst in line[:7]:
        if inst == 'F':
            top -= (top - bottom + 1) / 2
        elif inst == 'B':
            bottom += (top - bottom + 1) / 2
    row = bottom
    bottom = 0
    top = 7
    for inst in line[7:]:
        if inst == 'L':
            top -= (top - bottom + 1) / 2
        elif inst == 'R':
            bottom += (top - bottom + 1) / 2
    seats.append(row * 8 + bottom)

for i in range(127 * 8 + 7):
    if i not in seats and i - 1 in seats and i + 1 in seats:
        print(i)
