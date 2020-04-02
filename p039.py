# Implemented this Python solution after reading the 'Arithmetic Approach' on  https://www.mathblog.dk/project-euler-39-perimeter-right-angle-triangle/

till = 1001

max_solutions = -1
max_solutions_p = -1
for p in range(2, till, 2): # p can only be even
	number_solutions = 0
	for a in range(1, p//3+1):
		if (p*(p-2*a)) % (2*(p-a)) == 0: # the modulo needs to be 0 when b = (p*(p-2*a)) / (2*(p-a)) is an integer solution
			number_solutions += 1
	if number_solutions > max_solutions:
		max_solutions = number_solutions
		max_solutions_p = p

print(max_solutions_p)
