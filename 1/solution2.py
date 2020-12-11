with open('input.txt', 'r') as inp:
    numbers = list(map(lambda x : int(x), inp.read().split('\n')))
for count, i in enumerate(numbers):
    for j in range(count, len(numbers)):
        for k in range(j, len(numbers)):
            if i + numbers[j] + numbers[k] == 2020:
                print(i * numbers[j] * numbers[k])
