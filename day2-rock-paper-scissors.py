input_path = "input/day2.txt"
input_file = open(input_path, "r")

# points for choosing item
choice_dict = {
    "A": 1,
    "B": 2,
    "C": 3,
}

outcome_dict = {
    "X": "lose",
    "Y": "draw",
    "Z": "win",
}

# key beats value
beats_dict = {
    "A": "C",
    "B": "A",
    "C": "B",
}

# key loses to value
loses_dict = {
    "A": "B",
    "B": "C",
    "C": "A",
}

my_score = 0
for line in input_file.readlines():
    line = line.split()
    outcome = outcome_dict[line[1]]
    opponent_choice = line[0]

    if outcome == "draw":
        my_score += choice_dict[opponent_choice]
        my_score += 3
    elif outcome == "lose":
        my_score += choice_dict[beats_dict[opponent_choice]]
    elif outcome == "win":
        my_score += choice_dict[loses_dict[opponent_choice]]
        my_score += 6

print(my_score)
