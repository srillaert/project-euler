from collections import Counter

def load_file():
	numbers = list(map(int, open("p059.input", "r").read().split(",")))
	return numbers

if __name__ == "__main__":
	numbers = load_file()
	xors = list(ord(' ') ^ Counter(numbers[i::3]).most_common(1)[0][0] for i in range(3)) # assume that space is the most common character
	solution = sum(numbers[i] ^ xors[i % 3] for i in range(len(numbers)))
	print(solution)
	
