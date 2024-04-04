mod prime;

fn main() {
    let till: usize = 2_000_000;
    let is_prime = prime::get_is_prime_array(till);
    let mut sum: usize = 0;
    for i in 0..till {
        if is_prime[i] {
            sum += i;
        }
    }
    println!("{}", sum);
}