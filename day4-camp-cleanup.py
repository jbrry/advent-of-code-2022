input_path = "input/day4.txt"
input_file = open(input_path, "r")

nb = 0
for line in input_file.readlines():
    line = line.strip()
    left, right = line.split(",")
    lh, lt = left.split("-")
    rh, rt = right.split("-")
    lh, lt = int(lh), int(lt)
    rh, rt = int(rh), int(rt)

    left_range = range(lh, lt+1)
    right_range = range(rh, rt+1)

    # Part 2
    for x in left_range:
        if x in right_range:
            nb += 1
            break

    # Part 1:
    # rcontains = set(left_range).issubset(right_range)
    # lcontains = set(right_range).issubset(left_range)
    # if rcontains:
    #     nb+=1
    # elif lcontains:
    #     nb+=1

print(nb)
