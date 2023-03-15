matrix = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]
list_comp = [[element * 2 for element in row] for row in matrix]
print(list_comp)
