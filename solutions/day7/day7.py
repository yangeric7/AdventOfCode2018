import parse

input_expression = '''Step {before} must be finished before step {after} can begin.'''
requirements = open('input.txt').readlines()

def create_graph():
    graph = {}
    for req in requirements:
        i = parse.parse(input_expression, req)
        before = i['before']
        after = i['after']

        if before not in graph:
            graph[before] = []
        if after not in graph:
            graph[after] = [before]
        else:
            graph[after].append(before)
        
    return graph

def part1():
    graph = create_graph()
    order = ''
    candidates = []

    for key,value in graph.items():
        if len(value) == 0:
            candidates.append(key)

    while len(graph):
        next_point = min(candidates)
        order = order + next_point
        for key, value in graph.items():
            if next_point in value:
                value.remove(next_point)
            if len(value) == 0 and key not in candidates:
                candidates.append(key)

        candidates.remove(next_point)
        graph.pop(next_point, None)

    return order

def part2():
    graph = create_graph()
    

print(part1())

