from itertools import product

with open("inputs/day7.txt", "r") as f:
    inputLines = f.readlines()

def partOne():
    totalSum = 0

    for line in inputLines:
        correctSum = int(line.split(": ")[0])
        numbers = [int(num) for num in line.split(": ")[1].strip().split()]
        allPossibleCombinations = product("+*", repeat=len(numbers) - 1)

        for addMul in allPossibleCombinations:
            currentValue = numbers[0]
            for i, addOrMul in enumerate(addMul):
                if addOrMul == "+":
                    currentValue += numbers[i + 1]
                elif addOrMul == "*":
                    currentValue *= numbers[i + 1]

            if currentValue == correctSum:
                totalSum += correctSum
                break

    print(totalSum)

def partTwo():
    totalSum = 0

    for line in inputLines:
        correctSum = int(line.split(": ")[0])
        numbers = [int(num) for num in line.split(": ")[1].strip().split()]
        allPossibleCombinations = product("+*|", repeat=len(numbers) - 1)

        for addMulCon in allPossibleCombinations:
            currentValue = numbers[0]
            for i, addConMul in enumerate(addMulCon):
                if addConMul == "+":
                    currentValue += numbers[i + 1]
                elif addConMul == "*":
                    currentValue *= numbers[i + 1]
                elif addConMul == "|":
                    currentValue = int(str(currentValue) + str(numbers[i + 1]))

            if currentValue == correctSum:
                totalSum += correctSum
                break

    print(totalSum)

partOne()
partTwo()