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

def part2(tree):
    child, meta = tree[:2]
    tree = tree[2:]
    value = []

    for _ in range(child):
        child_value, tree = part2(tree)
        value.append(child_value)

    if child == 0:
        return sum(tree[:meta]), tree[meta:]
    else:
        return sum([value[x-1] for x in tree[:meta] if x <= len(value) and x > 0]), tree[meta:]
    

print(part1(input_tree))
print(part2(input_tree))