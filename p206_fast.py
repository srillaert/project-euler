# solution from incandenza on https://projecteuler.net/thread=206;page=2
# 'I seem to have used a different technique than I've seen so far.  Instead of brute force, I construct the number from right to left, making the observation that the last n digits of the square can only be affected by the last n digits of the original number.'
# Adapted for Python 3

def matches_pattern(n, length):
    match = 0

    for _ in range(0, (length+1)//2):
        if n % 10 != match:
            return False
        match = (match - 1) % 10
        n //= 100

    return True

def try_it(solution):
    length = len(solution)
    
    if length == 10:
        square = int(solution)*int(solution)
        if len(str(square)) > 19 or not matches_pattern(square, 19):
            return None
        return solution

    for new_digit in range(0, 10):
        new_solution = str(new_digit) + solution
        new_square = int(new_solution)*int(new_solution)
        if matches_pattern(new_square, length+1):
            result = try_it(new_solution)
            if result != None:
                return result

    return None

print(try_it(''))