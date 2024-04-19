mod prime_sieve;

fn is_truncable_prime(prime_sieve: &prime_sieve::PrimeSieve, n: usize) -> bool {
    if !prime_sieve.is_prime(n) { return false; }
    let mut power_of_10 = 10;
    while power_of_10 <= n {
        if !prime_sieve.is_prime(n/ power_of_10) { return false; }
        if !prime_sieve.is_prime(n% power_of_10) { return false; }
        power_of_10 *= 10;
    }
    true
}

fn main() {
    const EXCLUDED_UPPER_BOUND: usize = 1_000_000;
    let prime_sieve = prime_sieve::PrimeSieve::new(EXCLUDED_UPPER_BOUND);

    let solution: usize = (11..EXCLUDED_UPPER_BOUND)
        .step_by(2)
        .filter(|&n| is_truncable_prime(&prime_sieve, n))
        .sum();

    println!("{}", solution);
}