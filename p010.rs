mod prime_sieve;

fn main() {
    let sieve = prime_sieve::PrimeSieve::new(2_000_000);
    let sum: usize = sieve.get_primes().sum();
    println!("{}", sum);
}