from math import sqrt

def get_largest_prime_factor(number):
    till = sqrt(number)
    n = 2
    while n < till:
        while number % n == 0:
            number //= n
            till = sqrt(number)
        n += 1
    return number

if __name__ == "__main__":
    solution = get_largest_prime_factor(600851475143)
    print(solution)
