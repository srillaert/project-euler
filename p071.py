till = 10 ** 6

def numerator_just_below(denominator):
    dividend = denominator * 3    
    result = dividend // 7
    remainder = dividend % 7
    if remainder == 0:
        result -= 1
    return result

largest_n = 1
largest_d = till
for d in range(2, till + 1):
    n = numerator_just_below(d)
    is_larger = n * largest_d > d * largest_n
    if is_larger:
        largest_n = n
        largest_d = d
        
print(largest_n)