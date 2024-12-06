with open("inputs/day5.txt", "r") as f:
    input = f.read()

rulesFull, updatesFull = input.split("\n\n")

rules = [tuple(int(x) for x in line.split("|")) for line in rulesFull.splitlines()]
updates = [tuple(int(x) for x in line.split(",")) for line in updatesFull.splitlines()]

def isCorrect(update):
    pageIndexes = {page: i for i, page in enumerate(update)}
    for rule1, rule2 in rules:
        if rule1 in update and rule2 in update and pageIndexes[rule1] > pageIndexes[rule2]:
            return False
    return True


correctUpdates = [update for update in updates if isCorrect(update)]
answer = sum(update[len(update)//2] for update in correctUpdates)
print(answer)