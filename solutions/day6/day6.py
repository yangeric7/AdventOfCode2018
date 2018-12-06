import numpy as np
input = open('input.txt').readlines()
#input = open('test.txt').readlines()
#np.printoptions(threshold=np.nan)

def mdist(point_a, point_b):
    return abs((point_b[0] - point_a[0])) + abs((point_b[1] - point_a[1]))

def part1():
    grid_x = max([int(coord.split(',')[0]) for coord in input])
    grid_y = max([int(coord.split(',')[1]) for coord in input])

    grid = np.zeros((grid_x, grid_y))

    coord_list = [(int(coord.split(',')[0]),int(coord.split(',')[1])) for coord in input]

    #brute force create grid
    for x in range(grid_x):
        for y in range(grid_y):
            mhdist = [mdist((x,y), (coord[0], coord[1])) for coord in coord_list]
            m = min(mhdist)
            min_index = mhdist.index(m)
            min_list = [i for i in mhdist if i == m]
            if len(min_list) > 1:
                grid[x][y] = -1
            else:
                grid[x][y] = min_index

    area_count = [0 for i in range(len(input))]
    for x in range(grid_x):
        for y in range(grid_y):
            index_in_grid = int(grid[x][y])
            if index_in_grid == -1 or area_count[index_in_grid] == -1:
                pass
            elif x == 0 or x == grid_x-1 or y == 0 or y == grid_y-1:
                area_count[index_in_grid] = -1
            else:
                area_count[index_in_grid] += 1

    return max(area_count)

def part2():
    grid_x = max([int(coord.split(',')[0]) for coord in input])
    grid_y = max([int(coord.split(',')[1]) for coord in input])

    grid = np.zeros((grid_x, grid_y))

    coord_list = [(int(coord.split(',')[0]),int(coord.split(',')[1])) for coord in input]

    #brute force create grid
    for x in range(grid_x):
        for y in range(grid_y):
            mhdist = [mdist((x,y), (coord[0], coord[1])) for coord in coord_list]
            if sum(mhdist) >= 10000:
                grid[x][y] = 0
            else:
                grid[x][y] = 1

    return int(sum(np.sum(grid, axis=0)))

#print('Part 1 Answer: ' + str(part1()))
print('Part 2 Answer: ' + str(part2()))