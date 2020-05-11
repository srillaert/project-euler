from math import factorial

def factorial_digit_sum(n):
    result = 0
    while n > 0:
        result += factorial(n%10)
        n //= 10
    return result

def length_non_repeating_chain(n):
    chain = []
    while not n in chain:
        chain.append(n)
        n = factorial_digit_sum(n)
    return len(chain)

result = sum(1 for i in range(1, 10 ** 6) if length_non_repeating_chain(i) == 60)
print(result)