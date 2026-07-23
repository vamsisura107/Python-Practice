r = int(input("Enter number of rows: "))
c = int(input("Enter number of columns: "))
matrix = []
print("Enter the matrix elements row by row (space-separated):")
for i in range(r):
    row = list(map(int, input().split()))
    matrix.append(row)
max_ones_count = -1
best_row_index = -1
for i in range(len(matrix)):
    current_row = matrix[i]
    ones_count = 0
    for space in current_row:
        if space == 1:
            ones_count += 1
    if ones_count > max_ones_count:
        max_ones_count = ones_count
        best_row_index = i
print("Row with maximum parking spaces:", best_row_index)
