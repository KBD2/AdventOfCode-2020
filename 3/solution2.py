with open('input.txt', 'r') as inp:
    lines = inp.read().split('\n')

slopes = (
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2)
    )

total = 1
for slope in slopes:
    
    count = 0
    x = 0
    y = 0
    
    while y < len(lines) - 1:
        x = (x + slope[0]) % len(lines[0])
        y += slope[1]
        if lines[y][x] == '#':
            count += 1
            
    total *= count

print(total)
