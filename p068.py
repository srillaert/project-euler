from itertools import permutations 

def valid_solution(perm, n):
    # starting form the group of n with the numerically lowest external node
    for i in range(1, n):
        if perm[n] > perm[n + i]:
            return False
    # each line adding to the same sum
    sum = perm[0] + perm[1] + perm[n]
    for i in range(1, n):
        if perm[i] + perm[(i+1)%n] + perm[n+i] != sum:
            return False
    return True

def solutions_magic_ngon_ring(n):
    numbers = range(1, 2 * n + 1)
    perms = permutations(numbers) 
    for perm in perms:
        if valid_solution(perm, n):
            yield perm

def get_max_solution(solutions, n, length):
    max = 0
    for solution in solutions:
        string = ""
        for i in range(n):
            string += str(solution[n+i]) + str(solution[i]) + str(solution[(i+1)%n])
        if len(string) == length:
            number = int(string)
            if number > max:
                max = number
    return max

def test_3gon():
    solutions = list(solutions_magic_ngon_ring(3))
    assert len(solutions) == 8
    max_solution = get_max_solution(solutions, 3, 9)
    assert max_solution == 432621513

if __name__ == "__main__":
    solutions = list(solutions_magic_ngon_ring(5))
    max_solution = get_max_solution(solutions, 5, 16)
    print(max_solution)