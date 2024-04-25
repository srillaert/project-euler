from prime_sieve import PrimeSieve

sieve = PrimeSieve(100000)

def check_pattern(pattern):
    step = int("".join(map(lambda c: "1" if c == "*" else "0", pattern)))
    initial_digit = 1 if pattern[0] == "*" else 0
    stop_multiplier = 10 - initial_digit
    start = int(pattern.replace("*", str(initial_digit)))
    smallest = None
    count = 0
    for multiplier in range(0, stop_multiplier):
        generated_number = start + multiplier * step
        if sieve.is_prime(generated_number):
            if smallest == None:
                smallest = generated_number
            count += 1
    return smallest, count


print(check_pattern("*3"))
print(check_pattern("56**3"))
