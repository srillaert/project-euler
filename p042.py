import itertools

def get_word_value(word):
	return sum(ord(c) - ord('A') + 1 for c in word)

is_triangle_number = [False] * 1000
triangle_number = 1
for n in itertools.count(2):
	if (triangle_number >= len(is_triangle_number)):
		break;
	is_triangle_number[triangle_number] = True
	triangle_number += n

with open("p042.input", "r") as file:
	words = file.read().strip('"').split('","')

count = sum(1 for word in words if is_triangle_number[get_word_value(word)])
print(count)		
