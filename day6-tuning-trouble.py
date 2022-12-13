# packet is indicated by a sequence of four characters that are all different.

input_path = "input/day6.txt"
input_file = open(input_path, "r")

charset = set()
l = 0

# part 1
for line in input_file.readlines():
    for i, r in enumerate(range(len(line))):
        while line[r] in charset:
            charset.remove(line[l])
            l+=1
        charset.add(line[r])
        if len(charset) == 14:
            print(i+1)
            break
