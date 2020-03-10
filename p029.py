# Generate a list with the power terms
sequence = []
for a in range(2,101):
	for b in range(2,101):
		sequence.append(a**b)

# Count the distinct terms
sequence.sort()
previous = -1
count = 0
for i in range(0, len(sequence)):
	if sequence[i] != previous:
		count += 1
		previous = sequence[i]

print(count)
