with open("inputs/day6.txt", "r") as f:
    inputLines = f.readlines()

for y, line in enumerate(inputLines):
    if "^" in line:
        pos = [line.index("^"), y]

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