def largest_palindrome_product(digit_count_numbers):
    largest_palindrome = 0
    end = pow(10, digit_count_numbers - 1) - 1 # 99 for 3 digits
    start = end * 10 + 9 # 999 for 3 digits

    for a in range(start,end,-1):
        for b in range(start,a,-1):
            product = a * b
            if product <= largest_palindrome:
                break
            string = str(product)
            if string == string[::-1]:
                largest_palindrome = product
    return largest_palindrome

if __name__ == "__main__":
    solution = largest_palindrome_product(3)
    print(solution)
