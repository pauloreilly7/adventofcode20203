
def part_1(input_path):

    max_value_by_colour = {'red':12, 'green':13, 'blue':14}
    id_sum = 0

    with open(input_path) as input:
        for line in input:
            game_id, games = line.strip().split(': ')
            game_id = int(game_id[4:])
            is_valid = True
            for game in games.split('; '):
                for entry in game.split(', '):
                    value, colour = entry.split(' ')
                    if int(value) > max_value_by_colour[colour]:
                        is_valid = False
            if is_valid:
                id_sum += game_id

    return id_sum

def part_2(input_path):
    power_sum = 0
    with open(input_path) as input:
        for line in input:
            _, games = line.strip().split(': ')
            min_value_needed = {'red':0,'green':0,'blue':0}
            for game in games.split('; '):
                for entry in game.split(', '):
                    value, colour = entry.split(' ')
                    if int(value) > min_value_needed[colour]:
                        min_value_needed[colour] = int(value)
            power = 1
            for value in min_value_needed.values():
                power *= value
            power_sum += power

    return power_sum

if __name__ == '__main__':
    input_path = '.\\day-2\\input.txt'
    id_sum = part_1(input_path)
    power_sum = part_2(input_path)

    print(f'[Part 1] Sum of ids: {id_sum}')
    print(f'[Part 2] Sum of powers: {power_sum}')