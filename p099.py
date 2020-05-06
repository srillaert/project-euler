from math import log

lines = [tuple(map(int, line.split(","))) for line in open("p099.input")]
max_value = 0
line_index = 0
for i in range(len(lines)):
    base, exponent = lines[i]
    logarithm = exponent * log(base)
    if logarithm > max_value:
        max_value = logarithm
        line_index = i + 1
print(line_index)