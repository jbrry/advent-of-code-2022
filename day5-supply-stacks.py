input_path = "input/day5.txt"
input_file = open(input_path, "r")

# parse game
config = [next(input_file) for x in range(9)]

cols = [[] for x in range(9)]   

for i, x in enumerate(config):
    for j, (start, end) in enumerate(zip(range(0, 36, 4), range(4, 40, 4))):
        item = x[start:end]
        if item == "    ":
            continue
        cols[j].append(item[1:2])

empty_line = next(input_file)

# move n from a-1 to b-1
for instruction in input_file.readlines():
    instruction = instruction.strip()
    parts = instruction.split()
    amount, source, destination = int(parts[1]), int(parts[3]), int(parts[5])

    if amount > 1:
        stack = []
        for _ in range(amount):
            popped = cols[source-1].pop(0)
            stack.append(popped)
        cols[destination-1] = stack + cols[destination-1]
    else:
        popped = cols[source-1].pop(0)
        cols[destination-1].insert(0, popped)

output = ""
for k in range(len(cols)):
    output += cols[k].pop(0)
print(output)