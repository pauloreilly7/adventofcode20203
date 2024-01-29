sum = 0
#input_path = ".\\day-1\\input.txt"
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
        sum += int(str(firstdigit)+str(lastdigit))

print(sum)
            