with open('input.txt', 'r') as inp:
    passports = inp.read().split('\n\n')

needed = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')

count = 0
for passport in passports:
    bits = []
    for part in map(lambda x: x.split('\n'), passport.split()):
        bits += part
    count += 1
    for part in needed:
        found = False
        for check in bits:
            if check[:3] == part:
                found = True
                break
        if not found:
            count -= 1
            break

print(count)
