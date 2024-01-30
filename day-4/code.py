def part_1(input_path):   
    total_points = 0
    with open(input_path) as input:
        for line in input:
            _, game = line.strip().split(':')
            winning, playing = game.strip().split(' | ')
            winners = 0
            for number in playing.split():
                if number in winning.split():
                    winners += 1
            if winners > 0:
                total_points += 2**(winners-1)
    return total_points


def part_2(input_path):
    cards = list()
    with open(input_path) as input:
        cards = [line for line in input]
    
    amounts = [1,]*len(cards)

    for i, card in enumerate(cards):
        _, game = card.split(':')
        winning, playing = game.strip().split(' | ')
        winners = 0
        for number in playing.split():
            if number in winning.split():
                winners += 1
        for j in range(winners):
            amounts[i+j+1] += amounts[i]
    return sum(amounts)

if __name__ == '__main__':
    input_path = '.\\day-4\\input.txt'
    part_1_ans = part_1(input_path)
    part_2_ans = part_2(input_path)

    print(f'[Part 1] Total winning numbers: {part_1_ans}')
    print(f'[Part 2] Total cards won: {part_2_ans}')