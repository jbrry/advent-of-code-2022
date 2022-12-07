input_path = "input/day1.txt"
input_file = open(input_path, "r")

tmp = []
top_three = [0, 0, 0]

for line in input_file.readlines():
    if line.isspace():
        calories = sum(tmp)
        if calories > min(top_three):
            top_three[-1] = calories
            # sort the top three scores in decreasing order
            top_three.sort(reverse=True)
        tmp = []
    else:
        tmp.append(int(line))
 
input_file.close()

print(f"The max calories are {sum(top_three)}.")