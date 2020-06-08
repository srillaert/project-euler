# this solution uses a modification of the algorithm of the sieve of Eratosthenes to build up an array of euler totients
# this way we don't have to factorize the numbers 1 till 10 million
# for Euler's product formula see https://en.wikipedia.org/wiki/Euler%27s_totient_function
def find_solution(till):
    # build the phi list with all the euler totients from 0 to till
    phi = [i for i in range(0, till)] # initially we set phi[i] = i
    # this is the modified sieve of Eratosthenes
    for i in range(2, till):
        if phi[i] == i: # we didn't touch phi[i] yet, i is prime
            for j in range(2*i, till, i):
                phi[j] = (phi[j] // i) * (i - 1) # adjust phi(j) for all j that have i as a prime factor
            phi[i] = i - 1 # phi(p) = p - 1 if p is a prime

    # now we can find the result
    minimum = 10000
    minimum_n = 0
    for n in range(2, till):
        euler_totient = phi[n]
        if sorted(str(euler_totient)) == sorted(str(n)): # is a permutation
            ratio = n / euler_totient
            if ratio < minimum:
                #print(n, euler_totient)
                minimum = ratio
                minimum_n = n
    return minimum_n

if __name__ == "__main__":
    result = find_solution(10 ** 7)
    print(result)