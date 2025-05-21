import re

with open('EverybodyCodes/Inputs/2024Quest2Part1.txt') as f:
    lines = f.read().split('\n')
    checks = lines[0]
    checks = checks.split(',')
    phrase = lines[2]

with open('EverybodyCodes/Inputs/2024Quest2Part2.txt') as f:
    lines2 = f.read().split('\n')
    checks2 = lines2[0]
    checks2 = checks2.split(',')
    phrase2 = str(lines2[2:])
    phrase2 = phrase2.split(',')

# with open('EverybodyCodes/Inputs/2024Quest2Part3.txt') as f:
#     lines3 = f.read().split('\n')

def partOne():
    ans = 0

    for i in checks:
        res = re.findall(i, phrase)
        ans += len(res)

    print(f'Part One: {ans}')

def partTwo():
    ans = 0
    
    for i in phrase2:
        res = re.findall('|'.join(j for j in checks2), i)
        for i in res:
            ans += len(i)
        print(res)
        res = re.findall('|'.join(j for j in checks2), i[::-1])
        for i in res:
            ans += len(i)

    print(f'Part Two: {ans}')

def partThree():
    ans = 0

    print(f'Part Three: {ans}')

partOne()
partTwo()