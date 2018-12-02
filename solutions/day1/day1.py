import itertools

def part1(frequency_input):
    return sum(frequency_input)

def part2(frequency_input):
    total_frequency = 0
    seen_frequency = {0}

    for frequency in itertools.cycle(frequency_input):
        total_frequency += frequency
        if total_frequency in seen_frequency:
            return total_frequency
        seen_frequency.add(total_frequency)

def main():
    #test = ['+7', '+7', '-2', '-7', '-4']
    with open('input.txt', 'r') as input_file:
        input = input_file.readlines()

    frequency_list = [int(frequency) for frequency in input]

    print('Part 1 Answer: ' + str(part1(frequency_list)))
    print('Part 2 Answer: ' + str(part2(frequency_list)))

if __name__ == '__main__':
    main()