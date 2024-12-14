with open("inputs/day11.txt", "r") as f:
    input = f.read().strip()

numbers = input.split()

def blink(numbers):
    newNumbers = []
    for number in numbers:
        if number == "0":
            newNumbers.append("1")
        elif len(number) % 2 == 0:
            num1 = str(int(number[:len(number)//2]))
            num2 = str(int(number[len(number)//2:]))
            newNumbers.append(num1)
            newNumbers.append(num2)
        else:
            newNumbers.append(str(int(number)*2024))
    return newNumbers

newNumbers = numbers
for _ in range(25):
    newNumbers = blink(newNumbers)

print(len(newNumbers))