mod prime_sieve;

fn reverse(mut n: usize) -> usize {
    let mut result = 0;
    while n > 0 {
        result = result * 10 + n % 10;
        n /= 10;
    }
    result
}

fn is_reversable_prime_square(sieve: &prime_sieve::PrimeSieve, n: usize) -> bool {
    let rev = reverse(n);
    if rev == n {
        return false;
    }
    let sqrt_rev = (rev as f64).sqrt() as usize;
    return (sqrt_rev * sqrt_rev == rev) && sieve.is_prime(sqrt_rev);
}

#[test]
fn test_is_reversable_prime_square() {
    let mut sieve = prime_sieve::PrimeSieve::new(25);

    assert_eq!(is_reversable_prime_square(&mut sieve, 25), false);
    assert_eq!(is_reversable_prime_square(&mut sieve, 49), false, "reverse 94 is not the square of a prime");
    assert_eq!(is_reversable_prime_square(&mut sieve, 121), false, "121 is a palindrome");
    assert_eq!(is_reversable_prime_square(&mut sieve, 169), true);
    assert_eq!(is_reversable_prime_square(&mut sieve, 961), true);
}

fn main() {
    // The upper bound of 100 million was picked with trial and error.
    // Maybe replace with a dynamic growing prime sieve later ?
    let sieve = prime_sieve::PrimeSieve::new(100_000_000);

    let solution: usize = sieve.get_primes()
        .map(|p| p * p)
        .filter(|&ps| is_reversable_prime_square(&sieve, ps))
        .take(50)
        .sum();
    println!("{}", solution);
}