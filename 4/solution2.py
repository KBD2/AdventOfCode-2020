with open('input.txt', 'r') as inp:
    passports = inp.read().split('\n\n')

needed = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')

def validate(part, value):
    try:
        if part == 'byr':
            return 1919 < int(value) < 2003
        elif part == 'iyr':
            return 2009 < int(value) < 2021
        elif part == 'eyr':
            return 2019 < int(value) < 2031
        elif part == 'hgt':
            if value[-2:] == 'cm' \
            and int(value[:3]) > 149 \
            and int(value[:3]) < 194:
                return True
            elif value[-2:] == 'in' \
            and int(value[:2]) > 58 \
            and int(value[:2]) < 77:
                return True
        elif part == 'hcl':
            if value[0] != '#':
                return False
            for char in value[1:]:
                if char not in '0123456789abcdef':
                    return False
            return True
        elif part == 'ecl':
            return value in 'amb blu brn gry grn hzl oth'.split()
        elif part == 'pid':
            return len(value) == 9 and int(value) | 1
    except:
        return False

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
                if validate(part, check[4:]):
                    found = True
                    break
        if not found:
            count -= 1
            break

print(count)
