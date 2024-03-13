from prime import get_is_prime_array

def get_solution():
    # for how to calculate an upper bound, see the answer on https://math.stackexchange.com/questions/54312/non-trivial-upper-bound-for-the-number-of-primes-less-or-equal-to-n
    # for n = 105000 : (n / log(n)) * (1 + 1.2762/log(n)) == 10084.14889762712, more than 10001 so this is a good upper bound
    upper_bound = 105000
    prime_array = get_is_prime_array(upper_bound)
    counter = 0
    for i in range(len(prime_array)):
        if prime_array[i]:
            counter += 1
        if counter == 10001:
            return i

if __name__ == "__main__":
    solution = get_solution()
    print(solution)