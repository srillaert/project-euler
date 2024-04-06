mod prime;

fn main() {
    let till = 2_000_000;
    let is_prime = prime::get_is_prime_array(till);
    let sum: usize = (0..till).filter(|&i| is_prime[i]).sum();
    println!("{}", sum);
}