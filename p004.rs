fn reverse(mut n: u32) -> u32 {
    let mut result = 0;
    while n > 0 {
        result = result * 10 + n % 10;
        n /= 10;
    }
    result
}

fn largest_palindrome_product() -> u32 {
    let mut largest_palindrome: u32 = 0;
    for a in (100..=999).rev() {
        for b in (a..=999).rev() {
            let product = a * b;
            if product <= largest_palindrome {
                break;
            }
            if product == reverse(product) {
                largest_palindrome = product;
            }
        }
    }
    largest_palindrome
}

fn main() {
    let solution = largest_palindrome_product();
    println!("{solution}");
}