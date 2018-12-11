input_tree = [int(x) for x in open('input.txt').read().split()]

def part1(tree):
    child, meta = tree[:2]
    tree = tree[2:]
    total_sum = 0

    for _ in range(child):
        child_sum, tree = part1(tree)
        total_sum += child_sum

    total_sum += sum(tree[:meta])

    return total_sum, tree[meta:]

print(part1(input_tree))