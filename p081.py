import sys

matrix = [[int(number) for number in line.split(',')] for line in open('p081.input')]

def get_matrix_diagonal_item(diagonal_index, item_index):
    matrix_row = diagonal_index - item_index
    if matrix_row < 0 or matrix_row >= len(matrix):
        return sys.maxsize
    else:
        return matrix[matrix_row][item_index]

diagonal = [sys.maxsize] * len(matrix)
diagonal[0] = matrix[0][0]
for diagonal_index in range(1, 2 * len(matrix) - 1):
    for item_index in reversed(range(1, len(matrix))):
        diagonal[item_index] = get_matrix_diagonal_item(diagonal_index, item_index) + min(diagonal[item_index], diagonal[item_index - 1])
    diagonal[0] = get_matrix_diagonal_item(diagonal_index, 0) + diagonal[0]

print(diagonal[len(matrix) - 1])