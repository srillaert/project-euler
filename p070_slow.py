from functools import reduce # Valid in Python 2.6+, required in Python 3
import operator
from prime import get_factors

# def gcd(a, b):
#     if b > a:
#         a, b = b, a
#     while(b != 0):
#         a, b = b, a % b
#     return a

# def test_gcd():
#     assert gcd(9, 8) == 1
#     assert gcd(9, 6) == 3

# def euler_totient_function_old(n):
#     return sum(1 for i in range(2, n) if gcd(n, i) == 1) + 1

def euler_totient_function(n):
    factors = list(get_factors(n))
    result = n // reduce(operator.mul, factors, 1)
    result *= reduce(operator.mul, ((p - 1) for p in factors), 1) 
    return result

def test_euler_totient_function():
    assert euler_totient_function(9) == 6
    assert euler_totient_function(87109) == 79180

def find_solution(till):
    minimum = 10000
    minimum_n = 0
    for n in range(2, till):
        euler_totient = euler_totient_function(n)
        if sorted(str(euler_totient)) == sorted(str(n)): # is a permutation
            ratio = n / euler_totient
            if ratio < minimum:
                #print(n, euler_totient)
                minimum = ratio
                minimum_n = n
    return minimum_n

if __name__ == "__main__":
    result = find_solution(10000000)
    print(result)
