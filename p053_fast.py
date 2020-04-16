till = 100
count = 0
one_million = 10**6

# Initialize the first row of Pascal's triangle
row = [0] * (till + 1)
row[0] = 1

# Loop over all the n rows
for n in range(1, till + 1):
	for r in range(n, 0, -1):
		new_value = row[r] + row[r-1]
		if new_value > one_million:
			new_value = one_million # We are not interested in the exact values above one million, do less calculations with big integers
			count += 1
		row[r] = new_value
print(count)
