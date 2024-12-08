with open("inputs/day8.txt", "r") as f:
    inputLines = [line.strip() for line in f.readlines()]

letters = {}
antinodePositions = set()

for y in range(len(inputLines)):
    for x in range(len(inputLines[y])):
        char = inputLines[y][x]
        if char == ".":
            continue
        if char in letters.keys():
            letters[char].append((x,y))
        else:
            letters[char] = [(x,y)]

for letterPositions in letters.values():
    for posI in range(len(letterPositions)):
        for posJ in range(len(letterPositions)):
            if posI == posJ:
                continue
            pos1 = letterPositions[posI]
            pos2 = letterPositions[posJ]
            disX = pos2[0] - pos1[0] # right
            disY = pos2[1] - pos1[1] # down
            antinodePos1 = (pos1[0] - disX, pos1[1] - disY)
            antinodePos2 = (pos2[0] + disX, pos2[1] + disY)
            if 0 <= antinodePos1[0] < len(inputLines[0]) and 0 <= antinodePos1[1] < len(inputLines):
                antinodePositions.add(antinodePos1)
            if 0 <= antinodePos2[0] < len(inputLines[0]) and 0 <= antinodePos2[1] < len(inputLines):
                antinodePositions.add(antinodePos2) 

print(len(antinodePositions))