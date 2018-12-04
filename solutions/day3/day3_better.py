import numpy as np
import parse

claim_expression = '''#{id:d} @ {left:d},{top:d}: {width:d}x{height:d}\n'''
fabric = np.zeros((1000,1000), dtype=np.int)

def part1():
    for claim in open('input.txt'):
        c = parse.parse(claim_expression, claim)
        fabric[c['left'] : c['left'] + c['width'], c['top'] : c['top'] + c['height']] += 1

    return np.sum(np.where(fabric >= 2, 1, 0))

def part2():
    for claim in open('input.txt'):
        c = parse.parse(claim_expression, claim)
        if np.all(fabric[c['left'] : c['left'] + c['width'], c['top'] : c['top'] + c['height']] == 1):
            return c['id']
            

print('Part 1 Answer: ' + str(part1()))
print('Part 2 Answer: ' + str(part2()))
