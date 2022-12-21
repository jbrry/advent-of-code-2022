import numpy as np

input_path = "input/day8.txt"
input_file = open(input_path, "r")
lines = input_file.readlines()

# create a nested list that can be converted to numpy array
inputs = []
for line in lines:
    line = line.strip()
    inputs.append(list(line))

A = np.array(inputs)
highest_scenic_score = 0

for i, row in enumerate(A):
    # check elements from the LEFT
    scenic_left_scores = []
    lefts = []
    for r in range(len(row)):
        sl_score = 0
        lefts = row[:r]
        # reverse lefts, to iterate over them
        lefts = lefts[::-1]
        for l in lefts:
            if row[r] > l:
                sl_score +=1
            elif row[r] <= l:
                sl_score +=1
                break
        scenic_left_scores.append(sl_score)

    # check elements from the RIGHT
    scenic_right_scores = []
    for r in range(len(row)):
        sr_score = 0
        rights = row[r+1:]
        for j in rights:
            if row[r] > j:
                sr_score +=1
            elif row[r] <= j:
                sr_score += 1
                break
        scenic_right_scores.append(sr_score)

    # check elements from ABOVE and BELOW
    scenic_up_scores = []
    scenic_down_scores = []

    _, c = A.shape
    for column_index in range(c):
        grid_column = A[:, column_index] # all rows, specific column
        ups = grid_column[:i] # check everything above current row
        downs = grid_column[i+1:] # check everything below current row
        su_score = 0
        sd_score = 0

        target = A[i][column_index]

        # reverse ups, so we can iterate from above target to the edge
        ups = ups[::-1]
        for u in ups:
            if target > u:
                su_score += 1
            elif target <= u:
                su_score +=1
                break
        scenic_up_scores.append(su_score)

        for d in downs:
            if target > d:
                sd_score +=1
            elif target <= d:
                sd_score += 1
                break
        scenic_down_scores.append(sd_score)

    for l, r, u, d in zip(scenic_left_scores, scenic_right_scores, scenic_up_scores, scenic_down_scores):
        tmp = []
        if l != 0:
            tmp.append(l)
        if r != 0:
            tmp.append(r) 
        if u != 0:
            tmp.append(u)
        if d != 0:
            tmp.append(d)

        product = np.prod(tmp)
        if product > highest_scenic_score:
            highest_scenic_score = product

print(highest_scenic_score)

# PART 1:
# num_rows, num_cols = A.shape
# U = np.zeros(A.shape)
# for i, row in enumerate(A):
#     # first and last rows will always be visible, so skip them
#     if i == 0 or i == (num_rows -1):
#         continue

#     # check elements from the LEFT
#     lefts = []
#     l = 0
#     for r in range(1, len(row)):
#         lefts.append(row[l])
#         # check if element at index r is bigger than everything to the left
#         if row[r] > max(lefts):
#             if U[i][r] == 0:
#                 U[i][r] = 1
#         l += 1

#     # check elements from the RIGHT
#     rights = []
#     r = 1
#     for l in range(2, len(row)+1):
#         rights.append(row[-r])
#         if row[-l] > max(rights):
#             if U[i][-l] == 0:
#                 U[i][-l] = 1
#         r += 1

#    # check elements from ABOVE and BELOW
#     _, c = A.shape
#     for column_index in range(c):
#         grid_column = A[:, column_index] # all rows, specific column
#         ups = grid_column[:i] # check everything above current row
#         downs = grid_column[i+1:] # check everything below current row

#         target = A[i][column_index]
#         if target > max(ups):
#             if U[i][column_index] == 0:
#                 U[i][column_index] = 1

#         if target > max(downs):
#             if U[i][column_index] == 0:
#                 U[i][column_index] = 1

# # set all periphal (visible) items to 1
# U[:, 0] = 1
# U[:, -1] = 1
# U[0] = 1
# U[-1] = 1
# final = U.sum()

# print(final)