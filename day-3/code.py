def part_1(input_path):
    part_sum = 0
    chargrid = []
    symbol_ij = []
    with open(input_path) as input:
        chargrid = [[char for char in line.strip()] for line in input]
    
    m = len(chargrid)
    n = len(chargrid[0])

    for i in range(m):
        for j in range(n):
            if not chargrid[i][j].isdigit() and chargrid[i][j] != '.':
                symbol_ij.append((i,j))
    
    for i, j in symbol_ij:
        if i > 0 and j > 0 and chargrid[i-1][j-1].isdigit():
            part_sum += get_number(chargrid, i-1, j-1)
        if i > 0 and chargrid[i-1][j].isdigit():
            if j > 0 and not chargrid[i-1][j-1].isdigit():
                part_sum += get_number(chargrid, i-1, j)
        if i > 0 and j < n-1 and chargrid[i-1][j+1].isdigit():
            if not chargrid[i-1][j].isdigit():
                part_sum += get_number(chargrid, i-1, j+1)

        if j > 0 and chargrid[i][j-1].isdigit():
            part_sum += get_number(chargrid, i, j-1)
        if j < n-1 and chargrid[i][j+1].isdigit():
            part_sum += get_number(chargrid, i, j+1)
        
        if i < m-1 and j > 0 and chargrid[i+1][j-1].isdigit():
            part_sum += get_number(chargrid, i+1, j-1)
        if i < m-1 and chargrid[i+1][j].isdigit():
            if j > 0 and not chargrid[i+1][j-1].isdigit():
                part_sum += get_number(chargrid, i+1, j)
        if i < m-1 and j < n-1 and chargrid[i+1][j+1].isdigit():
            if not chargrid[i+1][j].isdigit():
                part_sum += get_number(chargrid, i+1, j+1)
    
    return part_sum

def part_2(input_path):
    chargrid = []
    symbol_ij = {}

    with open(input_path) as input:
        chargrid = [[char for char in line.strip()] for line in input]
    
    m = len(chargrid)
    n = len(chargrid[0])

    for i in range(m):
        for j in range(n):
            if chargrid[i][j] == '*':
                symbol_ij[(i,j)] = []
    
    for i, j in symbol_ij.keys():
        if i > 0 and j > 0 and chargrid[i-1][j-1].isdigit():
            symbol_ij[(i,j)].append(get_number(chargrid, i-1, j-1))
        if i > 0 and chargrid[i-1][j].isdigit():
            if j > 0 and not chargrid[i-1][j-1].isdigit():
                symbol_ij[(i,j)].append(get_number(chargrid, i-1, j))
        if i > 0 and j < n-1 and chargrid[i-1][j+1].isdigit():
            if not chargrid[i-1][j].isdigit():
                symbol_ij[(i,j)].append(get_number(chargrid, i-1, j+1))

        if j > 0 and chargrid[i][j-1].isdigit():
            symbol_ij[(i,j)].append(get_number(chargrid, i, j-1))
        if j < n-1 and chargrid[i][j+1].isdigit():
            symbol_ij[(i,j)].append(get_number(chargrid, i, j+1))
        
        if i < m-1 and j > 0 and chargrid[i+1][j-1].isdigit():
            symbol_ij[(i,j)].append(get_number(chargrid, i+1, j-1))
        if i < m-1 and chargrid[i+1][j].isdigit():
            if j > 0 and not chargrid[i+1][j-1].isdigit():
                symbol_ij[(i,j)].append(get_number(chargrid, i+1, j))
        if i < m-1 and j < n-1 and chargrid[i+1][j+1].isdigit():
            if not chargrid[i+1][j].isdigit():
                symbol_ij[(i,j)].append(get_number(chargrid, i+1, j+1))
    
    return sum([symbol_ij[(i,j)][0]*symbol_ij[(i,j)][1] for i,j in symbol_ij if len(symbol_ij[(i,j)]) == 2])

def get_number(chargrid, i, j):
    ans = ''
    while j >= 0 and chargrid[i][j].isdigit():
        j -= 1
    j += 1
    while j < len(chargrid[0]) and chargrid[i][j].isdigit():
        ans += chargrid[i][j]
        j += 1

    return int(ans)

if __name__ == '__main__':
    input_path = '.\\day-3\\input.txt'
    part_1_ans = part_1(input_path)
    part_2_ans = part_2(input_path)

    print(f'[Part 1] Sum of part numbers: {part_1_ans}')
    print(f'[Part 2] Sum of gear ratios: {part_2_ans}')