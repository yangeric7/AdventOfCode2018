input_statement = '468 players; last marble is worth 71010 points'

num_players = 468
last_marble = 71010

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
        
    return scores

print(max(part1()))