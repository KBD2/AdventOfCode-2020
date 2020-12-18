with open('input.txt', 'r') as inp:
    lines = inp.read().split('\n')

def evaluate(statement):
    lastOp = ''
    accumulator = 0
    index = 0
    while index < len(statement):
        char = statement[index]
        if char in '0123456789':
            if lastOp == '+' or lastOp == '':
                accumulator += int(char)
            elif lastOp == '*':
                accumulator *= int(char)
        elif char in '+*':
            lastOp = char
        elif char == '(':
            index += 1
            subStatement = ''
            level = 1
            while level > 0:
                subStatement += statement[index]
                if statement[index] == '(':
                    level += 1
                elif statement[index] == ')':
                    level -= 1
                index += 1
            subStatement = subStatement[:-1]
            if lastOp == '+' or lastOp == '':
                accumulator += evaluate(subStatement)
            elif lastOp == '*':
                accumulator *= evaluate(subStatement)
        index += 1
    return accumulator

total = 0
for line in lines:
    total += evaluate(line)
print(total)
