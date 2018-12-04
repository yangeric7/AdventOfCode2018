#how do i do this in a more pythonic way
def part1(fabric):
    num_overlap = 0
    for i in range(len(fabric)):
        for j in range(len(fabric[i])):
            if fabric[i][j] >= 2:
                num_overlap += 1

    return num_overlap

def part2(fabric, input_claim):
    overlap = False

    for claim in input_claim:
        id, left, top, width, height = get_claim(claim)
        for i in range(left, left + width):
            for j in range(top, top + height):
                if fabric[i][j] >= 2:
                    overlap = True
                    break
            if overlap:
                break
        
        if not overlap:
            return id
        else:
            overlap = False
    
    return None

#i hate O(n^3) -- probably more pythonic way maybe unavoidable for this
def create_fabric(input_claim):
    fabric = [[0]*1000 for _ in range(1000)]

    for claim in input_claim:
        _, left, top, width, height = get_claim(claim)
        for i in range(left, left + width):
            for j in range(top, top + height):
                fabric[i][j] += 1
            
    return fabric

def get_claim(raw_input):
    claims = raw_input.split(' ')
    id = claims[0].replace('#','')
    [left, top] = claims[2].replace(':','').split(',')
    [width, height] = claims[3].split('x')

    return int(id), int(left), int(top), int(width), int(height)


def main():
    with open('input.txt', 'r') as input_file:
        input = input_file.readlines()
    
    fabric = create_fabric(input)

    print('Part 1 Answer: ' + str(part1(fabric)))
    print('Part 2 Answer: ' + str(part2(fabric, input)))

if __name__ == '__main__':
    main()