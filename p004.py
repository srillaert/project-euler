def largest_product(start, stop, condition):
    largest_product = 0
    for a in range(start,stop,-1):
        for b in range(start,a-1,-1):
            product = a * b
            if product <= largest_product:
                break
            if condition(product):
                largest_product = product
    return largest_product

def is_palindrome(n):
    string = str(n)
    return string == string[::-1]

def largest_palindrome_product(digit_count_numbers):
    stop = pow(10, digit_count_numbers - 1) - 1 # 99 for 3 digits
    start = stop * 10 + 9 # 999 for 3 digits
    result = largest_product(start, stop, is_palindrome)
    return result

if __name__ == "__main__":
    solution = largest_palindrome_product(3)
    print(solution)
