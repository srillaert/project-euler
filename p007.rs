mod prime_sieve;

fn main() {
    // for how to calculate an upper bound, see the answer on https://math.stackexchange.com/questions/54312/non-trivial-upper-bound-for-the-number-of-primes-less-or-equal-to-n
    // for n = 105000 : (n / log(n)) * (1 + 1.2762/log(n)) == 10084.14889762712, more than 10001 so this is a good upper bound
    const EXCLUSIVE_UPPER_BOUND: usize = 105000;
    let sieve = prime_sieve::PrimeSieve::new(EXCLUSIVE_UPPER_BOUND);
    let element = sieve.get_primes().nth(10000); // Index is 0-based, so nth(10000) gives the 10001st prime

    match element {
        Some(value) => {
            println!("{}", value);
        }
        None => {
            println!("10001st prime number not found");
        }
    }
}