with open("inputs/day8.txt", "r") as f:
    inputLines = [line.strip() for line in f.readlines()]

letters = {}

for y in range(len(inputLines)):
    for x in range(len(inputLines[y])):
        char = inputLines[y][x]
        if char == ".":
            continue
        if char in letters.keys():
            letters[char].append((x,y))
        else:
            letters[char] = [(x,y)]

def partOne():
    antinodePositions = set()

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

def partTwo():
    antinodePositions = set()

    for letterPositions in letters.values():
        for posI in range(len(letterPositions)):
            for posJ in range(len(letterPositions)):
                if posI == posJ:
                    continue
                pos1 = letterPositions[posI]
                pos2 = letterPositions[posJ]
                disX = pos2[0] - pos1[0] # right
                disY = pos2[1] - pos1[1] # down
                allPoses = set()
                i = 0
                while True:
                    bothFalse = 0
                    antinodePos1 = (pos1[0] - disX*i, pos1[1] - disY*i)
                    antinodePos2 = (pos2[0] + disX*i, pos2[1] + disY*i)
                    if 0 <= antinodePos1[0] < len(inputLines[0]) and 0 <= antinodePos1[1] < len(inputLines):
                        allPoses.add(antinodePos1)
                    else:
                        bothFalse += 1
                    if 0 <= antinodePos2[0] < len(inputLines[0]) and 0 <= antinodePos2[1] < len(inputLines):
                        allPoses.add(antinodePos2) 
                    else:
                        bothFalse += 1
                    if bothFalse == 2:
                        break
                    i += 1
                for x in allPoses:
                    antinodePositions.add(x)

    print(len(antinodePositions))

partOne()
partTwo()