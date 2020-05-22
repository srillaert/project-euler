from prime import get_is_prime_array

till = 2000000
is_prime = get_is_prime_array(till - 1)
result = sum(n for n in range(1, till) if is_prime[n])
print(result)
