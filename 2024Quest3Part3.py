from copy import deepcopy

lines = open('EverybodyCodes/Inputs/2024Quest3Part3.txt').read().split()
grid = []

for i in lines:
    k = []
    for j in i:
        k.append(j)
    grid.append(k)

for x in range(len(grid)):
    for y in range(len(grid[0])):
        if grid[x][y] == '#':
            grid[x][y] = 1

for i in grid:
    i.append('.')
    i.insert(0, '.')
grid.append(['.'] * len(grid[0]))
grid.insert(0, ['.'] * len(grid[0]))

def partThree(grid):
    def checkAdj(x, y, newGrid):
        dirs = [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (1, 1), (-1, 1), (1, -1)]
        currNum = int(newGrid[x][y]) + 1

        for dx, dy in dirs:
            try:
                if newGrid[x + dx][y + dy] == '.':
                    return newGrid
                elif abs(newGrid[x + dx][y + dy] - currNum) > 1:
                    return newGrid
            except IndexError:
                continue
        newGrid[x][y] = currNum
        return newGrid
    
    running = True
    tempGrid = deepcopy(grid)
    while running:   
        for x in range(1, len(grid) - 1):
            for y in range(1, len(grid[0]) - 1):
                if grid[x][y] != '.':
                    grid = checkAdj(x, y, grid)
        if tempGrid == grid:
            running = False
        else:
            tempGrid = deepcopy(grid)

    ans = 0

    for i in grid:
        for j in i:
            if j != '.':
                ans += j

    print(f'Part Three: {ans}')

partThree(grid)