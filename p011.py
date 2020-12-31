from functools import reduce
import operator

result = 0
def process_four_elements(direction_array):
	global result
	product = reduce(operator.mul, direction_array[0:4], 1)
	result = max(result, product)

with open("p011.input") as input_file:
	array = list(int(w) for w in input_file.read().split())
for i in range(len(array)):
	process_four_elements(array[i::-19])
	process_four_elements(array[i::1])
	process_four_elements(array[i::21])
	process_four_elements(array[i::20])
print(result)
