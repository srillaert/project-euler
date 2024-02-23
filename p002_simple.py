def fibonacci_numbers(till):
    former_term, latter_term = 0, 1
    yield former_term
    while latter_term <= till:
        yield latter_term
        latter_term, former_term = latter_term + former_term, latter_term

result = sum(n for n in fibonacci_numbers(4000000) if n % 2 == 0)

print(result)
