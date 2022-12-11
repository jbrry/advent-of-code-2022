from string import ascii_lowercase as alc
from string import ascii_uppercase as ualc

input_path = "input/day3.txt"
input_file = open(input_path, "r")

lowers = {
    c: i + 1
    for i, c in enumerate(alc)
}

uppers = {
    c: i + 26 + 1
    for i, c in enumerate(ualc)
}


total_sum = 0

# Part 2:
new_group = []
character_stores = [set() for i in range(3)]
for i, line in enumerate(input_file.readlines(), start=1):
    line = line.strip()
    if i % 3 == 0:
        new_group.append(line)
        for j, inv in enumerate(new_group):
            for char in inv:
                character_stores[j].add(char)

        common = (set(character_stores[0]) & set(character_stores[1]) & set(character_stores[2])).pop()
        if common.isupper():
            item_priority = uppers[common]
        else:
            item_priority = lowers[common]
        total_sum += item_priority

        # reset items for next group of 3
        new_group = []
        character_stores = [set() for i in range(3)]
    else:
        new_group.append(line)
    
print(total_sum)


# Part 1:
# for line in input_file.readlines():
#     firsts = set()
#     seconds = set()
#     line = line.split().pop()
#     split_point = len(line) // 2
#     first_half = line[:split_point]
#     second_half = line[split_point:]

#     assert(len(first_half)==len(second_half))

#     for c in first_half:
#         firsts.add(c)
    
#     for c in second_half:
#         seconds.add(c)

#     for f in firsts:
#         for s in seconds:
#             if f==s:
#                 if f.isupper():
#                     item_priority = uppers[f]
#                 else:
#                     item_priority = lowers[f]
#                 total_sum += item_priority
# print(total_sum)
                
