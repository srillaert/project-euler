from math import sqrt

form = "1_2_3_4_5_6_7_8_9_0"
minimum_possible_form = int(form.replace("_","0"))
maximum_possible_form = int(form.replace("_","9"))

def get_candidates():
    n = int(sqrt(minimum_possible_form))
    stop = int(sqrt(maximum_possible_form))
    # 1) a solution needs to end with 0 to get 0 at the end of the square 
    # 2) the square of a number ending with 0 has 00 at the end
    # 3) a solution needs to end with 30 or 70 to get 900 at the end of the square
    n = (n // 100) * 100 + 30 # first candidate with 30 or 70 at the end
    while n <= stop:
        yield n # ending with 30
        yield n + 40 # ending with 70
        n += 100

def has_form(n):
    for d in range(10,1,-1):
        if n%10 != d%10:
            return False
        n //= 100
    return n == 1

if __name__ == "__main__":
    for n in get_candidates():
        if has_form(n*n):
            print(n)
            exit()

def test_has_form_minimum():
    assert(has_form(minimum_possible_form))