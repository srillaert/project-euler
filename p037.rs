mod prime;

fn is_truncable_prime(is_prime: &[bool], n: usize) -> bool {
    if !is_prime[n] { return false; }
    let mut power_of_10 = 10;
    while power_of_10 <= n {
        if !is_prime[n / power_of_10] { return false; }
        if !is_prime[n % power_of_10] { return false; }
        power_of_10 *= 10;
    }
    true
}

fn main() {
    const EXCLUDED_UPPER_BOUND: usize = 1_000_000;
    let mut is_prime_array = [true; EXCLUDED_UPPER_BOUND];
    prime::prime_sieve_initialize(&mut is_prime_array);

    let solution: usize = (11..EXCLUDED_UPPER_BOUND)
        .step_by(2)
        .filter(|&n| is_truncable_prime(&is_prime_array, n))
        .sum();

    println!("{}", solution);
}