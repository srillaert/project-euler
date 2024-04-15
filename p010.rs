mod prime;

fn main() {
    const EXCLUSIVE_UPPER_BOUND: usize = 2_000_000;
    let mut is_prime = [true; EXCLUSIVE_UPPER_BOUND];
    prime::prime_sieve_initialize(&mut is_prime);
    let sum: usize = (0..EXCLUSIVE_UPPER_BOUND).filter(|&i| is_prime[i]).sum();
    println!("{}", sum);
}