fn get_is_prime_array(till: usize) -> Vec<bool> {
    let mut result = vec![true; till + 1];
    result[0] = false;
    result[1] = false;
    let square_root = (till as f64).sqrt() as usize;    
    for i in 0..=square_root {
        if result[i] {
            for j in (i*i..=till).step_by(i) {
                result[j] = false;
            }
        }
    }
    result
}

fn get_solution()-> usize {
    // for how to calculate an upper bound, see the answer on https://math.stackexchange.com/questions/54312/non-trivial-upper-bound-for-the-number-of-primes-less-or-equal-to-n
    // for n = 105000 : (n / log(n)) * (1 + 1.2762/log(n)) == 10084.14889762712, more than 10001 so this is a good upper bound
    let upper_bound: usize = 105000;
    let is_prime_array = get_is_prime_array(upper_bound);
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