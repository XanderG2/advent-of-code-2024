import re
with open("inputs/day3.txt", "r") as f:
    input = f.read()

check = r"mul\(\d{1,3},\d{1,3}\)"
allCheck = r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)"

def partOne():
    commands = re.findall(check, input)

    sum = 0

    for command in commands:
        refined = command.replace("mul(", "").replace(")", "").split(",")
        number1 = int(refined[0])
        number2 = int(refined[1])
        product = number1 * number2
        sum += product

    print(sum)

def partTwo():
    commands = {match.start(): match.group()  for match in re.finditer(allCheck, input)}
    runCommands = []
    
    enabled = True

    for command in commands.values():
        if command == "do()":
            enabled = True
        elif command == "don't()":
            enabled = False
        else:
            if enabled:
                runCommands.append(command)

    sum = 0

    for command in runCommands:
        refined = command.replace("mul(", "").replace(")", "").split(",")
        number1 = int(refined[0])
        number2 = int(refined[1])
        product = number1 * number2
        sum += product
    
    print(sum)

    
        

#partOne()
partTwo()