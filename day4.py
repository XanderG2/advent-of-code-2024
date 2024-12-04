with open("inputs/day4.txt", "r") as f:
    inputLines = f.readlines()

directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]

def positionIsValid(x, y):
    return 0 <= y < len(inputLines) and 0 <= x < len(inputLines[y])

def checkDirection(dx, dy, x, y):
    positions = [(x + i * dx, y + i * dy) for i in range(4)]
    return all(
        positionIsValid(px, py) and inputLines[py][px] == "XMAS"[i]
        for i, (px, py) in enumerate(positions)
    )

xmases = 0

for y in range(len(inputLines)):
    for x in range(len(inputLines[y])):
        if inputLines[y][x] == "X":
            for dx, dy in directions:
                if checkDirection(dx, dy, x, y):
                    xmases += 1

print(xmases)