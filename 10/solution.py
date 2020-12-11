with open('input.txt', 'r') as inp:
    adaptors = inp.read().split('\n')

adaptors = list(map(lambda x: int(x), adaptors))
deviceJoltage = max(adaptors) + 3
differences = {1: 0, 3: 0}
currentJoltage = 0
while len(adaptors) > 0:
    selected = 0
    for count, adaptor in enumerate(adaptors):
        if adaptor > currentJoltage and adaptor < adaptors[selected]:
            selected = count
    differences[adaptors[selected] - currentJoltage] += 1
    currentJoltage = adaptors[selected]
    adaptors.pop(selected)

print(differences[1] * (differences[3] + 1))
