result = 0
a = 2
b = 1
for i in range(2, 1001):
    prev_a = a
    a = 2 * a + b
    b = prev_a
    # Numerator is a+b and denominator is a
    # print(a+b, a)
    if len(str(a+b)) > len(str(a)):
        result += 1
print(result)