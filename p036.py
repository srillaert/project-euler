def is_palindrome(string):
	return string[::-1] == string

def is_palindromic_in_either_base(n):
	return is_palindrome(str(n)) and is_palindrome("{0:b}".format(n))

result = sum(i for i in range(1, 10**6) if is_palindromic_in_either_base(i))

print(result)
