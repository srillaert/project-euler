def get_column(matrix, i):
    return [row[i] for row in matrix]

def add_vectors(vector_a, vector_b):
    return [sum(i) for i in zip(vector_a, vector_b)]

def minimal_path_sum(matrix):
    n = len(matrix)
    minimal = get_column(matrix, n-1)
    for i in range(n-2, 0, -1): # iterate over the middle columns from right to left
        column = get_column(matrix, i)
        minimal = add_vectors(minimal, column)
        for step in range(n-1):
            for j in range(1, n): # steps up
                minimal[j] = min(minimal[j], column[j] + minimal[j-1])
            for j in range(n-2, -1, -1): # steps down
                minimal[j] = min(minimal[j], column[j] + minimal[j+1])
    first_column = get_column(matrix, 0)
    minimal = add_vectors(minimal, first_column)    
    result = min(minimal)
    return result

def test_minimal_path_sum_down():
    matrix = [
        [1,1,4],
        [3,1,3],
        [4,1,1]
    ]
    assert minimal_path_sum(matrix) == 5

def test_minimal_path_sum_up():
    matrix = [
        [4,1,1],
        [3,1,3],
        [1,1,4]
    ]
    assert minimal_path_sum(matrix) == 5

if __name__ == "__main__":
    matrix = [[int(number) for number in line.split(',')] for line in open('p082.input')]
    print(minimal_path_sum(matrix))