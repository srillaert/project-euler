mod prime;

fn get_solution()-> usize {
    // for how to calculate an upper bound, see the answer on https://math.stackexchange.com/questions/54312/non-trivial-upper-bound-for-the-number-of-primes-less-or-equal-to-n
    // for n = 105000 : (n / log(n)) * (1 + 1.2762/log(n)) == 10084.14889762712, more than 10001 so this is a good upper bound
    const EXCLUSIVE_UPPER_BOUND: usize = 105000;
    let mut is_prime_array = [true; EXCLUSIVE_UPPER_BOUND];
    prime::initialize_is_prime_slice(&mut is_prime_array);
    let mut counter: usize = 0;
    for i in 0..=EXCLUSIVE_UPPER_BOUND {
        if is_prime_array[i] {
            counter += 1;
        }
        if counter == 10001 {
            return i;
        }
    }
    0
}

fn main() {
    let solution = get_solution();
    println!("{}", solution);
}