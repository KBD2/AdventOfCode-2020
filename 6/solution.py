with open('input.txt', 'r') as inp:
    groups = inp.read().split('\n\n')

total = 0
for group in groups:
    answers = group.split('\n')
    letters = set()
    for answer in answers:
        for char in answer:
            letters.add(char)
    total += len(letters)

print(total)
