# Based on https://blog.dreamshire.com/project-euler-81-solution/ and https://www.mathblog.dk/project-euler-81-find-the-minimal-path-sum-from-the-top-left-to-the-bottom-right-by-moving-right-and-down/
# This solution is easier to understand than my own original solution (see first commit of p081.py)
def get_minimal_path_sum(filename):
    with open(filename) as f:
        matrix = [list(map(int, line.split(','))) for line in f.readlines()]

    # Modify the matrix in-place, where each cell eventually contains the minimum path sum to reach that cell
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            # For each position (i,j), add to its current value the minimum of the value above or the value to the left
            matrix[i][j] += \
                min(matrix[i-1][j], matrix[i][j-1]) if i * j > 0 else \
                matrix[i-1][j] if i else \
                matrix[i][j-1] if j else \
                0

    return matrix[-1][-1]

if __name__ == "__main__":
    solution = get_minimal_path_sum("p081.input")
    print(solution)