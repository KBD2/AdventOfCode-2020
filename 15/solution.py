start = list(map(lambda x: int(x), input("Input? >").split(',')))

count = 1
spoken = {}
lastNum = start[-1]

for item in start[:-1]:
    spoken[item] = count
    count += 1

while count < 2020:
    if lastNum not in spoken:
        spoken[lastNum] = count
        lastNum = 0
    else:
        nextNum = count - spoken[lastNum]
        spoken[lastNum] = count
        lastNum = nextNum
    count += 1

print(lastNum)
