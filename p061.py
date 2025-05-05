def get_figurate_numbers_helper(generator):
	n = 1
	while True:
		square = generator(n)
		if square >= 10000:
			break
		if square >= 1000:
			yield square
		n += 1

def get_figurate_numbers(generators):
	return list((n, i) for i, g in enumerate(generators) for n in get_figurate_numbers_helper(g))

def get_cyclical_figurate_numbers(lookup, current, stop, visited_types):
	lookup_items = lookup.get(current%100)
	for lookup_item in lookup_items:
		n, pol_type = lookup_item
		if n == stop:
			if all(visited_types):
				return [current]
			else:
				return None
		elif visited_types[pol_type]:
			continue
		else:
			visited_types[pol_type] = True
			result = get_cyclical_figurate_numbers(lookup, n, stop, visited_types)
			if result != None:
				result.append(current)
				return result
			visited_types[pol_type] = False
	return None

def get_cyclical_figurate_numbers_from_list(figurative_numbers, types_count):
	lookup = dict()
	for n in range(100):
		lookup[n] = []
	for n, pol_type in figurative_numbers:
		lookup[n//100].append((n, pol_type))
	
	for lookup_value in lookup.values():
		for start, pol_type in lookup_value:
			visited_types = [False] * types_count
			visited_types[pol_type] = True
			result = get_cyclical_figurate_numbers(lookup, start, start, visited_types)
			if result != None:
				result.reverse()
				return result
	return result

if __name__ == "__main__":
	generators = [
		lambda n : n * (n + 1) // 2,
		lambda n : n * n,
		lambda n : n * (3 * n - 1) // 2,
		lambda n : n * (2 * n - 1),
		lambda n : n * (5 * n - 3) // 2,
		lambda n : n * (3 * n - 2),
	]
	figurate_numbers = get_figurate_numbers(generators)
	cyclical_figurate_numbers = get_cyclical_figurate_numbers_from_list(figurate_numbers, 6)
	solution = sum(cyclical_figurate_numbers)
	print(solution)