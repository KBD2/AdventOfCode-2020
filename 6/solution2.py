with open('input.txt', 'r') as inp:
    groups = inp.read().split('\n\n')

total = 0
for group in groups:
    answers = group.split('\n')
    letters = dict((char, 0) for char in "qwertyuiopasdfghjklzxcvbnm")
    for answer in answers:
        for char in answer:
            letters[char] += 1
    for letter in letters:
        if letters[letter] == len(answers):
            total += 1

print(total)
