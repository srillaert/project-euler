# Uses the more efficient method of only generating the even terms with the formula E(n) = 4 * E(n-1) + E(n-2)
former_term = 0
latter_term = 2
result = 0
while latter_term < 4000000:
    result += latter_term
    latter_term, former_term = 4 * latter_term + former_term, latter_term
print(result)
