with open("inputs/day11.txt", "r") as f:
    input = f.read().strip()

numbers = input.split()

cache = {}

def logic(number):
    if number in cache.keys():
        return cache[number]
    newNumbers = [] 
    if number == "0":
        newNumbers.append("1")
    else:
        n = len(number) 
        if n % 2 == 0:
            n2 = n//2
            num1 = str(int(number[:n2]))
            num2 = str(int(number[n2:]))
            newNumbers.append(num1)
            newNumbers.append(num2)
        else:
            newNumbers.append(str(int(number)*2024))
    cache[number] = newNumbers
    return newNumbers

def blink(numbers):
    newNumbers = []
    for number in numbers:
        newNumbers += logic(number)
    return newNumbers

def partOne():
    newNumbers = numbers
    for _ in range(25):
        newNumbers = blink(newNumbers)

    print(len(newNumbers))

def partTwo():
    newNumbers = numbers
    for _ in range(75):
        print(_)
        newNumbers = blink(newNumbers)

    print(len(newNumbers))

partOne()
partTwo()