# Compact solution inspired by https://github.com/nayuki/Project-Euler-solutions/blob/master/python/p052.py
number = 1
while not all(sorted(str(number)) == sorted(str(number * i)) for i in range(2,7)):
	number += 1
print(number)
