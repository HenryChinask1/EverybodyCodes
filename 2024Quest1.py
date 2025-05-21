with open('EverybodyCodes/Inputs/2024Quest1Part1.txt') as f:
    lines = f.read()
with open('EverybodyCodes/Inputs/2024Quest1Part2.txt') as f:
    lines2 = f.read()
with open('EverybodyCodes/Inputs/2024Quest1Part3.txt') as f:
    lines3 = f.read()

def partOne():
    potions = 0

    for i in lines:
        if i == 'B':
            potions += 1
        elif i == 'C':
            potions += 3

    print(f'Part One: {potions}')

def partTwo():
    potions = 0

    monsterGroups = [lines2[i:i + 2] for i in range(0, len(lines2), 2)]

    for i in monsterGroups:
        if 'x' not in i:
            potions += 2
        if i[0] == 'B':
            potions += 1
        if i[1] == 'B':
            potions += 1
        if i[0] == 'C':
            potions += 3
        if i[1] == 'C':
            potions += 3
        if i[0] == 'D':
            potions += 5
        if i[1] == 'D':
            potions += 5
        
    print(f'Part Two: {potions}')

def partThree():
    potions = 0

partOne()
partTwo()
partThree()