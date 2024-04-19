mod prime_sieve;

fn is_circular_prime(sieve: &prime_sieve::PrimeSieve, power_of_10: usize, n: usize) -> bool {
    let mut rotation = n;
    while sieve.is_prime(rotation) {
        rotation = (rotation % 10) * power_of_10 + rotation / 10;
        if rotation == n {
            return true;
        }
    }
    false
}

fn main() {
    let sieve = prime_sieve::PrimeSieve::new(1_000_000);
    let mut count = 4; // 4 circular primes below 10 : 2, 3, 5, 7
    for power_of_10 in (1..6).map(|x| 10usize.pow(x)) {
        for n in ((power_of_10 + 1)..(power_of_10 * 10)).step_by(2) {
            if is_circular_prime(&sieve, power_of_10, n) {
                count += 1;
            }
        }
    }
    println!("{}", count);
}