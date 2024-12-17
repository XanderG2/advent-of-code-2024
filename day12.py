import json

with open("inputs/day12.txt", "r") as f:
    inputLines = [line.strip() for line in f.readlines()]

DIRECTIONS = [(0, -1), (0, 1), (-1, 0), (1, 0)]

allexplored = set()
areas = {}

def validPos(x, y):
    return 0 <= y < len(inputLines) and 0 <= x < len(inputLines[0])

def canMove(x, y, letter):
    return validPos(x, y) and inputLines[y][x] == letter

def calculatePerimeter(coords, letter):
    perimeter = 0
    for x, y in coords:
        nonMoveablePoses = 0
        for dx, dy in DIRECTIONS:
            newPos = (x + dx, y + dy)
            if not canMove(*newPos, letter):
                nonMoveablePoses += 1
        perimeter += nonMoveablePoses
    return perimeter
        

def findAdjacent(x, y, letter):
    moveablePositions = []
    for dx, dy in DIRECTIONS:
        newPos = (x + dx, y + dy)
        if canMove(*newPos, letter):
            moveablePositions.append(newPos)
    return moveablePositions

def explore(x, y, letter):
    totalArea = set()
    stack = [(x, y)]
    allexplored.add((x, y))
    while stack:
        x2, y2 = stack.pop()
        totalArea.add((x2, y2))
        adjacent = findAdjacent(x2, y2, letter)
        for pos in adjacent:
            if pos not in allexplored:
                stack.append(pos)
                allexplored.add(pos)
    return list(totalArea)

def exploreAreas(x, y, letter):
    allCoords = explore(x, y, letter)
    area = len(allCoords)
    perimeter = calculatePerimeter(allCoords, letter)
    return area, perimeter, allCoords, letter

id = 0

for y, line in enumerate(inputLines):
    for x, char in enumerate(line):
        if (x, y) in allexplored:
            continue
        area, perimeter, allCoords, letter = exploreAreas(x, y, char)
        areas[id] = {"a": area, "p": perimeter, "c": allCoords, "l": letter}
        id += 1

total = 0

for stats in areas.values():
    total += stats["a"] * stats["p"]

print(total)
