# Used for problem 18 and 67
def get_maximum_path_sum(filename):
	array = []
	with open(filename) as input_file:
		for line in input_file:
			array.append([int(x) for x in line.split()])
	for row_index in range(len(array)-2, -1, -1):
		for column_index in range(0,len(array[row_index])):
			array[row_index][column_index] += max(array[row_index+1][column_index], array[row_index+1][column_index+1])
	return array[0][0]
