from math import factorial

factorials = [factorial(i) for i in range(10)]
def factorial_digit_sum(n):
    result = 0
    while n > 0:
        result += factorials[n%10]
        n //= 10
    return result

length_cache = {}
def length_non_repeating_chain(n):
    chain = []
    while not n in chain and not n in length_cache:
        chain.append(n)
        n = factorial_digit_sum(n)
    length = len(chain) + length_cache.get(n, 0)
    for i in range(1, len(chain)):
        length_cache[chain[i]] = length - i
    return length

result = sum(1 for i in range(1, 10 ** 6) if length_non_repeating_chain(i) == 60)
print(result)