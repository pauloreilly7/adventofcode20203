def part_1(input_path):
    races = []
    with open(input_path) as file:
        for line in file:
            races.append([int(entry) for entry in line.split(':')[1].strip().split()])
    races = list(zip(races[0],races[1]))

    ans = 1

    for time, dist in races:
        dists = [i*(time-i) for i in range(time+1) if i*(time-i) > dist]
        ans *= len(dists)
    return ans


def part_2(input_path):
    races = []
    with open(input_path) as file:
        for line in file:
            races.append(''.join(line.split(':')[1].strip().split()))
    count = 0
    time = int(races[0])
    dist = int(races[1])
    for i in range(time + 1):
        if i*(time-i) > dist:
            count += 1
    return count

if __name__ == '__main__':
    input_path = '.\\day-6\\input.txt'
    part_1_ans = part_1(input_path)
    part_2_ans = part_2(input_path)

    print(f'[Part 1] Product of ways to win: {part_1_ans}')
    print(f'[Part 2] Number of ways to win: {part_2_ans}')