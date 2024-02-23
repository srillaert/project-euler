# Uses the more efficient method of only generating the even fibanacci numbers with the formula E(n) = 4 * E(n-1) + E(n-2)
def even_fibonacci_numbers(till):
    former_term, latter_term = 0, 2
    yield former_term
    while latter_term <= till:
        yield latter_term
        latter_term, former_term = 4 * latter_term + former_term, latter_term

result = sum(n for n in even_fibonacci_numbers(4000000))

print(result)

