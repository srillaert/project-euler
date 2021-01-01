import functools

@functools.lru_cache(maxsize=None) # Python 3.2, see https://stackoverflow.com/questions/1988804/what-is-memoization-and-how-can-i-use-it-in-python
def length_collatz_sequence(n):
	if n == 1:
		return 1
	if n % 2 == 0:
		return length_collatz_sequence(n / 2) + 1 # n is even
	else:
		return length_collatz_sequence((3 * n + 1) / 2) + 2 # n is odd, then 3*n+1 is even on which we can immediately apply the next step of dividing by 2

maximum_length = 0
maximum_starting_number = 0
for starting_number in range(1, 1000000):
	length = length_collatz_sequence(starting_number)
	if length > maximum_length:
		maximum_length = length
		maximum_starting_number = starting_number
print(maximum_starting_number)
