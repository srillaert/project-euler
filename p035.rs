mod prime;

fn is_circular_prime(is_prime: &[bool], power_of_10: usize, n: usize) -> bool {
    let mut rotation = n;
    while is_prime[rotation] {
        rotation = (rotation % 10) * power_of_10 + rotation / 10;
        if rotation == n {
            return true;
        }
    }
    false
}

fn main() {
    let is_prime = prime::get_is_prime_array(1_000_000);
    let mut count = 4; // 4 circular primes below 10 : 2, 3, 5, 7
    for power_of_10 in (1..6).map(|x| 10usize.pow(x)) {
        for n in ((power_of_10 + 1)..(power_of_10 * 10)).step_by(2) {
            if is_circular_prime(&is_prime, power_of_10, n) {
                count += 1;
            }
        }
    }
    println!("{}", count);
}