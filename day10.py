with open("inputs/day10.txt", "r") as f:
    inputLines = [[int(char) for char in line.strip()] for line in f.readlines()]


def findTrailheads():
    trailheads = []
    for x, row in enumerate(inputLines):
        for y, char in enumerate(row):
            if char == 0:
                trailheads.append((x, y))
    return trailheads

def canMove(x, y, prev_height):
    return 0 <= x < len(inputLines) and 0 <= y < len(inputLines[0]) and inputLines[x][y] == prev_height + 1

def trailhead_score(start):
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
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            x2, y2 = x + dx, y + dy
            if canMove(x2, y2, inputLines[x][y]):
                placesToCheck.append((x2, y2))
    return len(nines)

trailheads = findTrailheads()
totalScore = sum(trailhead_score(start) for start in trailheads)

print(totalScore)
