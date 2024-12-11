# doesnt work but cba to find an answer

with open("inputs/day9.txt", "r") as f:
    diskmap = f.read()

fileBlocks = {}
id = 0

for i in range(0, len(diskmap), 2):
    if i+1 >= len(diskmap):
        fileBlocks.update({id: int(diskmap[i])})
        continue
    fileBlocks.update({id: int(diskmap[i]), f"s{id}": int(diskmap[i+1])})
    id += 1

fileBlocks2 = dict(fileBlocks)

for id, space in fileBlocks.items():
    if space == 0:
        fileBlocks2.pop(id)

visualisation = "".join([str(id)*space if isinstance(id, int) else "."*space for id, space in fileBlocks2.items()])

visualisation = list(visualisation)

for x in range(len(visualisation) - 1, -1, -1):
    lastChar = visualisation[x]
    if lastChar == ".":
        continue
    for y in range(len(visualisation)):
        firstChar = visualisation[y]
        if firstChar == ".":
            visualisation[y] = lastChar
            visualisation[x] = "."
            break

visualisation = "".join(visualisation)[1:] + "."

checksum = 0

for position, id in enumerate(visualisation):
    if id == ".":
        continue
    checksum += position*int(id) 

print(checksum)
