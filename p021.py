def sum_proper_divisors(n):
    sum = 0
    till = n//2
    for i in range(1, till+1):
        if n%i == 0:
            sum += i
    return sum

def is_amicable_number(n):
    sum = sum_proper_divisors(n)
    return sum != n and sum_proper_divisors(sum) == n

sum = 0
for n in range(1, 10000):
    if is_amicable_number(n):
        #print(n)
        sum += n
print(sum)
