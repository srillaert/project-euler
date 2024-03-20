/// Uses the sieve of Eratosthenes to generate a Vec<bool> where indices represent numbers and values indicate primality.
pub fn get_is_prime_array(till: usize) -> Vec<bool> {
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