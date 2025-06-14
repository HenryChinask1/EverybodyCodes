file = open('EverybodyCodes/Inputs/2024Quest5TEST.txt').read().split()
clappers = [[], [], [], []]

for idx, num in enumerate(file):
    clappers[idx % 4].append(num)

print(clappers)

def partOne():
    turns = [0, 1, 2, 3]
    ans = 0


    print(f'Part One: {ans}')

partOne()