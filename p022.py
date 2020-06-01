def get_alphabetical_value(name):
	return sum(ord(c) - ord('A') + 1 for c in name)

names = open('p022.input').read().replace('"','').split(',')
names.sort()
total_names_score = sum(position * get_alphabetical_value(name) for position, name in enumerate(names, 1))
print(total_names_score)
