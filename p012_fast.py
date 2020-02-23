def prime_factors(n):
    i = 2
    while i*i <= n:
        while n%i == 0:
            yield i
            n //= i
        i += 1
    if n != 1:
        yield n

def prime_factor_exponents(n):
    current_factor = 0
    count = 0
    for p in prime_factors(n):
        if p != current_factor and current_factor != 0:
            yield count
            count = 0
        current_factor = p
        count += 1
    yield count

def number_of_divisors(n):
    product = 1
    for e in prime_factor_exponents(n):
        product *= (e + 1)
    return product

count = 0
n = 0
i = 0
while count < 500:
    i += 1
    n += i
    count = number_of_divisors(n)
print(n)
