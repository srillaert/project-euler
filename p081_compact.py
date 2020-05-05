# Based on https://blog.dreamshire.com/project-euler-81-solution/ and https://www.mathblog.dk/project-euler-81-find-the-minimal-path-sum-from-the-top-left-to-the-bottom-right-by-moving-right-and-down/
# This solution is more compact than my own original solution in p081.py
matrix = [list(map(int, line.split(','))) for line in open("p081.input").readlines()]

for i in range(len(matrix)):
    for j in range(len(matrix)):
        matrix[i][j] += \
            min(matrix[i-1][j], matrix[i][j-1]) if i * j > 0 else \
            matrix[i-1][j] if i else \
            matrix[i][j-1] if j else \
            0

print(matrix[-1][-1])