with open('input.txt', 'r') as inp:
    numbers = list(map(lambda x : int(x), inp.read().split('\n')))
for count, i in enumerate(numbers):
    for j in range(count, len(numbers)):
        if i + numbers[j] == 2020:
            print(i * numbers[j])
