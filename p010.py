from prime_sieve import PrimeSieve

till = 2000000
sieve = PrimeSieve(till)
result = sum(n for n in range(1, till) if sieve.is_prime(n))
print(result)
