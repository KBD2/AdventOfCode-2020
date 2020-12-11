with open('input.txt', 'r') as inp:
    adaptors = inp.read().split('\n')

adaptors = list(map(lambda x: int(x), adaptors))

cache = {}

def branch(current):
    subtotal = 0
    possible = []
    
    for count, adaptor in enumerate(adaptors):
        if current < adaptor < current + 4:
            possible.append(count)
            
    if len(possible) == 0:
        subtotal += 1
    for item in possible:
        if adaptors[item] in cache:
            subtotal += cache[adaptors[item]]
        else:
            subtotal += branch(adaptors[item])

    cache[current] = subtotal
    
    return subtotal

print(branch(0))
