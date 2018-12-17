input = '286051'
input_index = 286051
list_input = map(int, str(input))

scores = '37'
first_elf = 0
second_elf = 1

def get_scores(scores, first_elf, second_elf, number):
    while input not in scores[-7:]:
        new_recipe = int(scores[first_elf]) + int(scores[second_elf])
        scores += str(new_recipe)
        
        first_elf = (first_elf + 1 + int(scores[first_elf])) % len(scores)
        second_elf = (second_elf + 1 + int(scores[second_elf])) % len(scores)

    return scores

scores = get_scores(scores, first_elf, second_elf, input_index + 10)

#Part 1
print(scores[input_index : input_index + 10])

#Part 2
print(scores.index(input))
