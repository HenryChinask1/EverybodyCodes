file = open('EverybodyCodes/Inputs/2024Quest5TEST.txt').read().split()
clappers = [[], [], [], []]

for idx, num in enumerate(file):
    clappers[idx % 4].append(num)

def partOne():
    ans = 0

    print(f'Part One: {ans}')

partOne()