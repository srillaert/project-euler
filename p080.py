from decimal import *
getcontext().prec = 110 # precision higher than digits needed to avoid rounding up of significant digits

def add_to_sum_digits(n):
    d = Decimal(n).sqrt()
    digits = d.to_eng_string()
    if (digits.find('.') == -1):
        return 0
    digit_count = 0
    sum = 0
    for i, v in enumerate(digits):
        if (v != '.'):
            sum += int(v) 
            digit_count += 1
        if (digit_count >= 100):
            break
    return sum

def test_example():
    assert add_to_sum_digits(2) == 475

def test_perfect_square():
    assert add_to_sum_digits(25) == 0

if __name__ == "__main__":
    sum_digits = 0
    for n in range(100):
        sum_digits += add_to_sum_digits(n)
    print(sum_digits)
