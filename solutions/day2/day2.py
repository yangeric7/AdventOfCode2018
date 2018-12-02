def part1(id_list):
    exactly_two = 0
    exactly_three = 0

    for id in id_list:
        two, three = find_count(id)
        exactly_two += two
        exactly_three += three
    
    return exactly_two * exactly_three

def part2(id_list):
    for id1 in id_list:
        for id2 in id_list:
            if id1 != id2:
                diff_list = [char[0] != char[1] for char in zip(list(id1.strip()), list(id2.strip()))]
                if sum(diff_list) == 1:
                    common = [char[0] for char in zip(list(id1.strip()), list(id2.strip())) if char[0] == char[1]]
                    return ''.join(common)
            else:
                pass

# feel like this can be improved
def find_count(id):
    seen = {}
    exactly_two = False
    exactly_three = False
    for character in id:
        if character in seen:
            seen[character] += 1
        else:
            seen[character] = 1
    
    for _, value in seen.items():
        if value == 2:
            exactly_two = True
        elif value == 3:
            exactly_three = True
    
    return exactly_two, exactly_three

def main():
    with open('input.txt', 'r') as input_file:
        input = input_file.readlines()
    
    print('Part 1 Answer: ' + str(part1(input)))
    print('Part 2 Answer: ' + str(part2(input)))

if __name__ == "__main__":
    main()