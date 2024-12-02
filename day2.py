with open("inputs/day2.txt", "r") as f:
    inputLines = f.readlines()

safeTotal = 0

for line in inputLines:
    reports = [int(x) for x in line.split()]
    previousReport = None
    increase = None
    safe = True
    for report in reports:
        if increase == None:
            if previousReport:
                if previousReport > report: 
                    increase = False
                elif previousReport == report:
                    safe = False
                else: 
                    increase = True
        if previousReport and (increase != None):
            if previousReport > report and increase == True:
                safe = False
            elif previousReport < report and increase == False:
                safe = False
            elif previousReport == report:
                safe = False
            elif increase and (previousReport <= report - 4):
                safe = False
            elif (not increase) and (previousReport >= report + 4):
                safe = False
        #print(f"{report}, {'safe' if safe else 'unsafe'}, increased by: {report - previousReport if not previousReport == None else "nope"}")
        previousReport = report
    #print(f"safe: {safe}, {'increase' if increase else 'decrease'}")
    if safe:
        safeTotal += 1
        #print(f"safe. {safeTotal} times")

print(safeTotal)

