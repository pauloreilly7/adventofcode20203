def part_1(input_path):
    winnings = 0
    hands = {}

    cards = '23456789TJQKA'
    card_val = {card:i for i, card in enumerate(cards,1)}

    with open(input_path) as file:
        for line in file:
            hand, rank = line.strip().split()
            hands[hand] = int(rank)
    
    sorted_hands = sorted(hands.keys(),key=lambda x: (
        score(x), 
        card_val[x[0]],
        card_val[x[1]],
        card_val[x[2]],
        card_val[x[3]],
        card_val[x[4]],
        ))

    for i, hand in enumerate(sorted_hands, 1):
        winnings += hands[hand] * i
    return winnings

def part_2(input_path):
    winnings = 0
    hands = {}

    cards = 'J23456789TQKA'
    card_val = {card:i for i, card in enumerate(cards,1)}

    with open(input_path) as file:
        for line in file:
            hand, rank = line.strip().split()
            hands[hand] = int(rank)
    
    sorted_hands = sorted(hands.keys(),key=lambda x: (
        score_jokers(x), 
        card_val[x[0]],
        card_val[x[1]],
        card_val[x[2]],
        card_val[x[3]],
        card_val[x[4]],
        ))

    for i, hand in enumerate(sorted_hands, 1):
        winnings += hands[hand] * i
    return winnings

def score(hand):

    cards = {}
    for card in hand:
        if card in cards:
            cards[card] += 1
        else:
            cards[card] = 1

    if len(cards) == 1:
        return 6
    if len(cards) == 2:
        if 4 in cards.values():
            return 5
        return 4
    if len(cards) == 3:
        if 3 in cards.values():
            return 3
        return 2
    if len(cards) == 4:
        return 1
    return 0

def score_jokers(hand):

    cards = {}
    for card in hand:
        if card in cards:
            cards[card] += 1
        else:
            cards[card] = 1
    
    if 'J' in cards and len(cards) > 1:
        cards.pop('J')
        card = ''
        max_val = 0
        for c in cards:
            if cards[c] > max_val:
                max_val = cards[c]
                card = c

        return score(hand[::].replace('J',card))

    if len(cards) == 1:
        return 6
    if len(cards) == 2:
        if 4 in cards.values():
            return 5
        return 4
    if len(cards) == 3:
        if 3 in cards.values():
            return 3
        return 2
    if len(cards) == 4:
        return 1
    return 0

if __name__ == '__main__':
    input_path = '.\\day-7\\input.txt'
    part_1_ans = part_1(input_path)
    part_2_ans = part_2(input_path)

    print(f'[Part 1] Total winnings: {part_1_ans}')
    print(f'[Part 2] Total winnings: {part_2_ans}')