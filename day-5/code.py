def part_1(input_path):
    min_value = 100000000000
    almanac = []
    with open(input_path) as input:
        almanac = ''.join([line for line in input])
    
    seeds, *rng_maps = almanac.split('\n\n')
    seeds = [int(seed) for seed in seeds.split(': ')[1].split()]
    for i, rng_map in enumerate(rng_maps[::]):
        rng_maps[i] = [tuple([int(value) for value in rng.split()]) for rng in rng_map.split('\n')[1:]]
    
    for seed in seeds:
        for rng_map in rng_maps:
            seed = apply_map_to_value(rng_map, seed)
        if seed < min_value:
            min_value = seed
    return min_value

def part_2(input_path):
    min_value = 100000000000
    almanac = []
    with open(input_path) as input:
        almanac = ''.join([line for line in input])
    
    seeds, *rng_maps = almanac.split('\n\n')
    seeds = [int(seed) for seed in seeds.split(': ')[1].split()]
    seeds = [(seeds[i],seeds[i]+seeds[i+1]-1) for i in range(len(seeds)) if i%2==0]

    for i, rng_map in enumerate(rng_maps[::]):
        rng_maps[i] = [tuple([int(value) for value in rng.split()]) for rng in rng_map.split('\n')[1:]]

    print(seeds)
    print('-----')
    for rng_map in rng_maps:
        seeds = apply_map_to_range(rng_map, seeds[::])
        print(seeds)
        print(rng_map)
        print('---------')
    
    for seed in seeds:
        if seed[0] < min_value:
            min_value = seed[0]
    
    return min_value

def apply_map_to_value(rng_map, value):
    for rng in rng_map:
        if value >= rng[1] and value <= rng[1]+rng[2]: 
            return rng[0] - rng[1] + value
    return value

def apply_map_to_range(rng_map, seeds):
    ## given a list of range maps and one seed
    ## 1. if seed not in any of the range maps -> return seed
    ## 2. if seed fully encompassed in a range map -> return encompassed seed, break
    ## 3. if seed partially encompassed in range map -> return encompassed part, check
    ## remaining maps for leftover part
    arr = []
    for seed in seeds:
        ans = []
        leftover = []
        j = 0
        for i, rng in enumerate(rng_map):

            if seed[0] > rng[1] + rng[2]-1 or seed[1] < rng[1]:
                continue

            if seed[0] >= rng[1] and seed[1] <= rng[1] + rng[2]-1:
                ans = (rng[0] - rng[1] + seed[0], rng[0] - rng[1] + seed[1])
                break

            if seed[0] < rng[1] and seed[1] > rng[1] + rng[2]-1:
                ans = (rng[0], rng[0]+rng[2]-1)
                leftover.append((seed[0],rng[1]-1))
                leftover.append((rng[1]+rng[2],seed[1]))
                j = i
                break

            if seed[0] < rng[1]:
                ans = (rng[0], rng[0]-rng[1]+seed[1])
                leftover.append((seed[0],rng[1]-1))
                j = i
                break

            if seed[1] > rng[1] + rng[2]-1:
                ans = (rng[0]-rng[1]+seed[0], rng[0]+rng[2]-1)
                leftover.append((rng[1]+rng[2],seed[1]))
                j = i
                break

        if ans == []:
            ans = seed
        if leftover != [] and j<len(rng)-1:
            arr.extend(apply_map_to_range(rng_map[j+1:],leftover[::]))
        arr.append(ans)
    return arr

if __name__ == '__main__':
    input_path = '.\\day-5\\input.txt'
    part_1_ans = part_1(input_path)
    part_2_ans = part_2(input_path)

    print(f'[Part 1] : {part_1_ans}')
    print(f'[Part 2] : {part_2_ans}')

