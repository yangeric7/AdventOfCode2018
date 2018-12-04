#i really hate O(n^3) and i want to fix
def part1(claim_array):
    fabric = [[0]*1000 for _ in range(1000)]

    for claim in claim_array:
        id, left, top, width, height = get_claim(claim)
        for i in range(left, left + width):
            for j in range(top, top + height):
                fabric[i][j] += 1
    
    num_overlap = 0
    for i in range(len(fabric)):
        for j in range(len(fabric[i])):
            if fabric[i][j] >= 2:
                num_overlap += 1

    return num_overlap

def main():
    with open('input.txt', 'r') as input_file:
        input = input_file.readlines()
    
    print('Part 1 Answer: ' + str(part1(input)))

def get_claim(raw_input):
    claims = raw_input.split(' ')
    id = claims[0].replace('#','')
    [left, top] = claims[2].replace(':','').split(',')
    [width, height] = claims[3].split('x')

    return int(id), int(left), int(top), int(width), int(height)

if __name__ == '__main__':
    main()