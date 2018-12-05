polymer = open('input.txt').read().strip()
alphabet = 'abcdefghijklmnopqrstuvwxyz'

def remove_collisions(polymer):
    index = 0
    while index < len(polymer) - 1:
        first = polymer[index]
        second = polymer[index + 1]
        if first.lower() == second.lower() and first != second:
            polymer = polymer[:index] + polymer[index + 2:]
            index = max(index-1,0)
        else:
            index += 1

    return polymer

print('Part 1 Answer: ' + str(len(remove_collisions(polymer))))

shortest = len(polymer)
for letter in alphabet:
    new_polymer = polymer.replace(letter,'').replace(letter.upper(), '')
    size = len(remove_collisions(new_polymer))
    if size < shortest:
        shortest = size

print('Part 2 Answer: ' + str(shortest))
