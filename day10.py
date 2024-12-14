with open("inputs/day10.txt", "r") as f:
    inputLines = [[int(char) for char in line.strip()] for line in f.readlines()]

DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def findTrailheads():
    trailheads = []
    for x, row in enumerate(inputLines):
        for y, char in enumerate(row):
            if char == 0:
                trailheads.append((x, y))
    return trailheads

def canMove(x, y, prevHeight):
    return validPos(x, y) and inputLines[x][y] == prevHeight + 1

def validPos(x, y):
    return 0 <= x < len(inputLines) and 0 <= y < len(inputLines[0])

def trailheadScore(start):
    visited = set()
    placesToCheck = [start]
    nines = set()

    while len(placesToCheck) != 0:
        x, y = placesToCheck.pop()
        if (x, y) in visited:
            continue
        visited.add((x, y))
        if inputLines[x][y] == 9:
            nines.add((x, y))
        for dx, dy in DIRECTIONS:
            x2, y2 = x + dx, y + dy
            if canMove(x2, y2, inputLines[x][y]):
                placesToCheck.append((x2, y2))
    return len(nines)

def countPaths(x, y, height):
    if not canMove(x, y, height):
        return False
    if inputLines[x][y] == 9:
        return True
    totalPaths = 0
    for dx, dy in DIRECTIONS:
        totalPaths += countPaths(x + dx, y + dy, inputLines[x][y])

    return totalPaths

def findAmountOfPaths(trailhead):
    x, y = trailhead
    return countPaths(x, y, -1)

def partOne():
    trailheads = findTrailheads()
    totalScore = sum(trailheadScore(start) for start in trailheads)

    print(totalScore)

def partTwo():
    trailheads = findTrailheads()
    totalRating = sum(findAmountOfPaths(start) for start in trailheads)
    print(totalRating)

partOne()
partTwo()