from parse import parse

input = open('input.txt').readlines()
rules_expression = '{in} => {out}'

initial_state = input[0].split(':')[1].strip()
rules = {}
for a in input[2:]:
    rules[parse(rules_expression, a)['in']] = parse(rules_expression, a)['out']

def part1():
    initial_index = 0
    current_string = initial_state
    for _ in range(20):
        current_string = '..' + current_string + '..'
        initial_index += 2
        read_state = '..' + current_string + '..'
        next_gen = ''
        for index in range(len(current_string)):
            substring = read_state[index:index+5]
            next_gen = next_gen + rules[substring]

        current_string = next_gen

    pots_index = [i - initial_index for i in range(len(current_string)) if current_string[i] == '#']

    return sum(pots_index)


# after many iterations, this pattern converges to the same pattern, with just a different initial index
def find_pattern():
    initial_index = 0
    current_string = initial_state
    final_index = 0
    for i in range(1000):
        current_string = '..' + current_string + '..'
        initial_index += 2
        read_state = '..' + current_string + '..'
        next_gen = ''
        for index in range(len(current_string)):
            substring = read_state[index:index+5]
            next_gen = next_gen + rules[substring]

        start = 0
        end = len(next_gen) - 1

        while next_gen[start] == '.':
            start += 1
            initial_index -= 1
        while next_gen[end] == '.':
            end -= 1
        
        current_string = next_gen[start:end+1]
        
        print(current_string, initial_index,i+1)
        print()
        final_index = i + 1

    return current_string, initial_index, final_index

def part2():
    current_string, initial_index, final_index = find_pattern()
    initial_index = -50000000000 + (initial_index + final_index)
    pots_index = [i - initial_index for i in range(len(current_string)) if current_string[i] == '#']

    return sum(pots_index)

print(part1())
print(part2())
