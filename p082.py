def add_vectors(vector_a, vector_b):
    return [a + b for a, b in zip(vector_a, vector_b)]

def get_minimal_path_sum(rows):
    columns = list(map(list, zip(*rows))) # transpose rows to columns
    n = len(columns)
    minimal = columns[0]
    for column in columns[1:-1]:
        minimal = add_vectors(minimal, column)
        for j in range(1, n): # move up
            minimal[j] = min(minimal[j], column[j] + minimal[j-1])
        for j in reversed(range(n - 1)): # move down
            minimal[j] = min(minimal[j], column[j] + minimal[j+1])
    minimal = add_vectors(minimal, columns[-1])
    result = min(minimal)
    return result

def get_minimal_path_sum_from_file(filename):
    with open(filename) as f:
        rows = [list(map(int, line.strip().split(','))) for line in f]
    return get_minimal_path_sum(rows)

if __name__ == "__main__":
    solution = get_minimal_path_sum_from_file('p082.input')
    print(solution)
