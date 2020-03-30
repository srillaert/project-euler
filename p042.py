def get_word_value(s):
	sum = 0
	for c in s:
		value = ord(c) - ord('A') + 1
		sum += value
	return sum

with open("p042.input", "r") as file:
	content = file.read()
words = content.strip('"').split('","')

is_triangle_number = [False] * 1000
n = 1
triangle_number = n * (n+1) // 2
while(triangle_number < len(is_triangle_number)):
	is_triangle_number[triangle_number] = True
	n += 1
	triangle_number = n * (n+1) // 2

count = 0
for word in words:
	word_value = get_word_value(word)
	if is_triangle_number[word_value]:
		count += 1

print(count)		
