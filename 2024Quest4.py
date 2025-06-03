import statistics

f = open('EverybodyCodes/Inputs/2024Quest4Part1.txt').read().split()
for i in range(len(f)):
    f[i] = int(f[i])

nails = open('EverybodyCodes/Inputs/2024Quest4Part2.txt').read().split()
for i in range(len(nails)):
    nails[i] = int(nails[i])

nails3 = open('EverybodyCodes/Inputs/2024Quest4Part3.txt').read().split()
for i in range(len(nails3)):
    nails3[i] = int(nails3[i])

def partOne():
    ans = 0
    deepestNail = min(f)
    for i in f:
        ans += i - deepestNail
    print(f'Part One: {ans}')

def partTwo():
    ans = 0
    deepestNail = min(nails)

    for i in nails:
        ans += i - deepestNail
    print(f'Part Two: {ans}')

def partThree():
    ans = 0
    meanNail = statistics.mean(nails3)

    for i in nails3:
        ans += abs(i - meanNail)
    print(f'Part Three: {ans}')

partOne()
partTwo()
partThree()