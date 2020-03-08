with open('p022.input') as file:
	names = file.read().replace('"','').split(',')
names.sort()

total_names_score = 0
substract_value = ord('A') - 1
for i in range(0, len(names)):
	name = names[i]
	alphabetical_value = 0
	for j in range(0, len(name)):
		alphabetical_value += ord(name[j]) - substract_value  
	name_score = alphabetical_value * (i + 1)
	total_names_score += name_score

print(total_names_score)
