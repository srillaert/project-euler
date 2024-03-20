mod prime;

fn get_solution()-> usize {
    // for how to calculate an upper bound, see the answer on https://math.stackexchange.com/questions/54312/non-trivial-upper-bound-for-the-number-of-primes-less-or-equal-to-n
    // for n = 105000 : (n / log(n)) * (1 + 1.2762/log(n)) == 10084.14889762712, more than 10001 so this is a good upper bound
    let upper_bound: usize = 105000;
    let is_prime_array = prime::get_is_prime_array(upper_bound);
    let mut counter: usize = 0;
    for i in 0..=upper_bound {
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