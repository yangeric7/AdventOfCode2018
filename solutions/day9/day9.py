from collections import deque

input_statement = '468 players; last marble is worth 71010 points'

num_players = 468
last_marble = 71010
last_marble_p2 = last_marble * 100

# elves were definitely amused at this solution :3
def part1():
    scores = [0 for i in range(num_players)]
    game = [0]
    marble_index = 0
    player_index = 0

    for i in range(1, last_marble + 1):
        if i % 23 == 0:
            scores[player_index] += i
            marble_index = (marble_index - 7) % len(game)
            scores[player_index] += game.pop(marble_index)
        else:
            new_index = (marble_index + 2) % len(game)
            game.insert(new_index, i)
            marble_index = new_index

        player_index = (player_index + 1) % num_players
        
    return max(scores)

def part2():
    scores = [0 for i in range(num_players)]
    game = deque([0])
    player_index = 0

    for i in range(1, last_marble_p2 + 1):
        if i % 23 == 0:
            game.rotate(-7)
            scores[player_index] += (i + game.pop())
        else:
            game.rotate(2)
            game.append(i)

        player_index = (player_index + 1) % num_players

    return max(scores)

print(part1())
print(part2())