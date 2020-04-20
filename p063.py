from itertools import count

result = sum(
    next(exponent for exponent in count(1)
        if len(str(number ** exponent)) != exponent) - 1
    for number in range(1,10))
print(result)