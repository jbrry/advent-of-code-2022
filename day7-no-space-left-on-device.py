from collections import defaultdict
import operator

input_path = "input/day7.txt"
input_file = open(input_path, "r")
lines = input_file.readlines()

d = defaultdict(int)
path = []

for line in lines:
    line = line.strip()
    parts = line.split()

    # change directory
    if parts[1] == "cd":
        destination = parts[-1]
        if destination == "/":
            path = ["/"]
        elif destination == "..":
            path.pop() # move back
        else:
            path.append(destination)
    else:
        # one-liner to check if first part can be converted to int (file line)
        size = int(parts[0]) if parts[0].isdecimal() else None
        if size:
            # based on https://www.youtube.com/watch?v=6nbNRzSg7CA&ab_channel=MeeralQ
            for i in range(len(path)):
                if i <= 1:
                    d[path[i]] += size
                else:
                    parent = path[i-1]
                    current = path[i]
                    directory_key = f"{parent}/{current}"
                    d[directory_key] += size

# Part 1:
less_than_limit_sum = 0
for size in d.values():
    if size <= 100000:
        less_than_limit_sum += size
print(less_than_limit_sum)

# Part 2
total_space = 70000000
unused_space_required = 30000000
used_space = total_space - d["/"]
to_delete = abs(used_space - unused_space_required)

_min = 100000000000
answer = 0
for k, v in d.items():
    abs_diff = abs(to_delete - v)
    print(abs_diff, v)
    if abs_diff < _min:
        _min = abs_diff
        answer = v
print(answer)