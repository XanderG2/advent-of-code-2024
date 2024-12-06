from collections import defaultdict, deque

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

def partOne():
    correctUpdates = [update for update in updates if isCorrect(update)]
    answer = sum(update[len(update)//2] for update in correctUpdates)
    print(answer)

def sort(pages, rules):
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    pages_set = set(pages)

    for rule1, rule2 in rules:
        if rule1 in pages_set and rule2 in pages_set:
            graph[rule1].append(rule2)
            in_degree[rule2] += 1
            in_degree.setdefault(rule1, 0)

    queue = deque([node for node in pages if in_degree[node] == 0])
    sorted_pages = []

    while queue:
        current = queue.popleft()
        sorted_pages.append(current)
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return sorted_pages if len(sorted_pages) == len(pages) else []

def partTwo():
    incorrect_updates = [update for update in updates if not isCorrect(update)]
    corrected_updates = [sort(update, rules) for update in incorrect_updates]
    middle_pages = [update[len(update) // 2] for update in corrected_updates]
    print(sum(middle_pages))
            
partOne()
partTwo()