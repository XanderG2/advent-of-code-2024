with open("inputs/day2.txt", "r") as f:
    inputLines = f.readlines()

def everyLine(line):
    reports = [int(x) for x in line.split()]
    previousReport = None
    increase = None
    safe = True
    safeDampened = 0
    for report in reports:
        if increase == None:
            if previousReport:
                if previousReport > report: 
                    increase = False
                elif previousReport == report:
                    safe = False
                    safeDampened += 1
                else: 
                    increase = True
        if previousReport and (increase != None):
            if (previousReport > report and increase == True) or (previousReport < report and increase == False) or (previousReport == report) or (increase and (previousReport <= report - 4)) or (not increase) and (previousReport >= report + 4):
                safe = False
        previousReport = report
    return safe

def partOne():
    safeTotal = 0
    for line in inputLines:
        safeTotal += everyLine(line)
    print(safeTotal)

def partTwo():
    safeTotal = 0
    for line in inputLines:
        if everyLine(line):
            safeTotal += 1
            continue
        for i in range(len(line)):
            if everyLine(line[:i-1] + line[i+1:]):
                safeTotal += 1
                break
    print(safeTotal)



partOne()
partTwo()

