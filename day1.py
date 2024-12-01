with open("inputs/day1.txt", "r") as f:
    inputLines = f.readlines()

leftList = []
rightList = []

for line in inputLines:
    x = line.split("   ")
    leftList.append(int(x[0]))
    rightList.append(int(x[1]))

leftList.sort(); rightList.sort()

pairs = zip(leftList, rightList)

sum = 0

for n in pairs:
    difference = abs(n[0] - n[1])
    sum += difference

print(sum)