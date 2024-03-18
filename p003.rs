fn get_largest_prime_factor(mut number: u64)-> u64 {
    let mut till = (number as f64).sqrt() as u64;
    let mut divisor = 2;
    while divisor <= till {
        while number % divisor == 0 {
            number = number / divisor;
            till = (number as f64).sqrt() as u64;
        }
        divisor += 1;
    }
    number
}

fn main() {
    let number = 600851475143;
    let solution = get_largest_prime_factor(number);
    println!("{solution}");
}