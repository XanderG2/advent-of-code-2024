import json

with open("inputs/day11.txt", "r") as f:
    input = f.read().strip()

numbers = input.split()

cache = {}


def corelogic(number):
    if number in cache.keys():
        return cache[number]
    newNumbers = {}
    if number == "0":
        newNumbers["1"] = 1
    else:
        n = len(number) 
        if n % 2 == 0:
            n2 = n // 2
            num1 = str(int(number[:n2]))
            num2 = str(int(number[n2:]))
            if not num1 == num2:
                newNumbers[num1] = 1
                newNumbers[num2] = 1
            else:
                newNumbers[num1] = 2
        else:
            newNumbers[str(int(number) * 2024)] = 1
    cache[number] = newNumbers
    return newNumbers

def logic(number, amount):
    o = corelogic(number)
    return {key: amount * value for key, value in o.items()}

def merge(newNumbers, o):
    for key, value in o.items():
        if key in newNumbers:
            newNumbers[key] += value
        else:
            newNumbers[key] = value
    return newNumbers

def blink(numbers):
    newNumbers = {}
    for number, amount in numbers.items():
        o = logic(number, amount)
        newNumbers = merge(newNumbers, o)
    return newNumbers

def partOne():
    newNumbers = {x: 1 for x in numbers}
    json_formatted_str = json.dumps(newNumbers, indent=2)
    print(json_formatted_str)
    for _ in range(25):
        newNumbers = blink(newNumbers)
    print(sum(newNumbers.values()))

def partTwo():
    newNumbers = {x: 1 for x in numbers}
    for _ in range(75):
        newNumbers = blink(newNumbers)

    print(sum(newNumbers.values()))

partOne()
partTwo()