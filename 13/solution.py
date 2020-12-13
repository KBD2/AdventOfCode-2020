with open('input.txt', 'r') as inp:
    lines = inp.read().split('\n')

start = int(lines[0])
busses = list(map(lambda x: int(x), filter(lambda x: x != 'x', lines[1].split(','))))

earliestBus = [0, 1e99]

for bus in busses:
    wait = bus * (start // bus + 1) - start
    if wait < earliestBus[1]:
        earliestBus = [bus, wait]

print(earliestBus[0] * earliestBus[1])
