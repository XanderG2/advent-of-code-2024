import re
with open("inputs/day3.txt", "r") as f:
    input = f.read()

check = r"mul\(\d{1,3},\d{1,3}\)"

commands = re.findall(check, input)

sum = 0

for command in commands:
    refined = command.replace("mul(", "").replace(")", "").split(",")
    number1 = int(refined[0])
    number2 = int(refined[1])
    product = number1 * number2
    sum += product

print(sum)