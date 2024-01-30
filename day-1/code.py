
def part_1(input_path):

    digits_sum = 0

    with open(input_path) as input:
        for line in input:
            firstdigit = 0
            lastdigit = 0
            for character in line.strip():
                if character.isdigit():
                    if firstdigit <= 0:
                        firstdigit = int(character)
                    else:
                        lastdigit = int(character)
            if lastdigit <= 0:
                lastdigit = firstdigit
            digits_sum += int(str(firstdigit)+str(lastdigit))

    return digits_sum

def part_2(input_path):
    digits_sum = 0
    numbers_map = {
        'one':1,
        'two':2,
        'three':3,
        'four':4,
        'five':5,
        'six':6,
        'seven':7,
        'eight':8,
        'nine':9,
    }

    with open(input_path) as input:
        for line in input:
            firstdigit = 0
            lastdigit = 0
            newline = line.strip()
            for num in numbers_map:
                newline = newline.replace(num,num[0]+str(numbers_map[num])+num[-1])
            for character in newline:
                if character.isdigit():
                    if firstdigit <= 0:
                        firstdigit = int(character)
                    else:
                        lastdigit = int(character)
            if lastdigit <= 0:
                lastdigit = firstdigit
            digits_sum += int(str(firstdigit)+str(lastdigit))

    return digits_sum

if __name__ == '__main__':
    input_path = '.\\day-1\\input.txt'
    digit_sum = part_1(input_path)
    digit_sum_2 = part_2(input_path)

    print(f'[Part 1] Sum of digits: {digit_sum}')
    print(f'[Part 2] Sum of digits: {digit_sum_2}')