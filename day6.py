with open("inputs/day6.txt", "r") as f:
    inputLines = f.readlines()

for y, line in enumerate(inputLines):
    if "^" in line:
        pos = [line.index("^"), y]

def partOne():
    dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    dir_index = 0
    visited = set()
    moving = True

    while moving:
        visited.add(tuple(pos))
        nextX = pos[0] + dirs[dir_index][0]
        nextY = pos[1] + dirs[dir_index][1]
        if nextY < 0 or nextY >= len(inputLines) or nextX < 0 or nextX >= len(inputLines[0]):
            break
        if inputLines[nextY][nextX] == "#":
            dir_index = (dir_index + 1) % len(dirs)
        else:
            pos[0] = nextX
            pos[1] = nextY

    print(len(visited))

def simulateGuard(inputLines, obstruction):
    inputLines = [list(line) for line in inputLines]
    dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    dirI = 0

    for y, row in enumerate(inputLines):
        for x, val in enumerate(row):
            if val == "^":
                startPos = (x, y)

    if obstruction:
        inputLines[obstruction[1]][obstruction[0]] = "#"

    visited = set()
    pos = startPos
    while True:
        posdir = (pos[0], pos[1], dirI)
        if posdir in visited:
            return True
        visited.add(posdir)
        nextX = pos[0] + dirs[dirI][0]
        nextY = pos[1] + dirs[dirI][1]
        if nextY < 0 or nextY >= len(inputLines) or nextX < 0 or nextX >= len(inputLines[0]):
            return False
        if inputLines[nextY][nextX] == "#":
            dirI = (dirI + 1) % 4
        else:
            pos = (nextX, nextY)

def partTwo():
    possible_positions = []
    for y, row in enumerate(inputLines):
        for x, val in enumerate(row):
            if val == ".":
                if simulateGuard(inputLines, obstruction=(x, y)):
                    possible_positions.append((x, y))
    print(len(possible_positions))

partOne()
partTwo()