from prime import is_prime

primes_count = 3
numbers_count = 5
right_bottom_corner = 9
current_add = 2
while primes_count * 100 // numbers_count >= 10:
    current_add += 2
    numbers_count += 4    
    extra_primes_count = sum(
        1 for n in range(
            right_bottom_corner + current_add, 
            right_bottom_corner + 4 * current_add + 1, 
            current_add)
            if is_prime(n))
    right_bottom_corner += 4 * current_add
    primes_count += extra_primes_count
side_length = current_add + 1
print(side_length)