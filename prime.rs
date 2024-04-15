/// Uses the sieve of Eratosthenes to generate a Vec<bool> where indices represent numbers and values indicate primality.
#[allow(dead_code)]
pub fn get_is_prime_vector(exclusive_upper_bound: usize) -> Vec<bool> {
    let mut result = vec![true; exclusive_upper_bound];
    prime_sieve_initialize(&mut result);
    result
}

// The slice needs to be pre-filled with true values
// Runs the sieve of Eratosthenes where indices represent numbers and values indicate primality
// Using a slice allows the sieve to be used with both compiled time allocated arrays and dynamically allocated vectors
pub fn prime_sieve_initialize(slice: &mut [bool]) {
    slice[0] = false;
    slice[1] = false;
    let square_root = ((slice.len() - 1) as f64).sqrt() as usize;
    for i in 0..=square_root {
        if slice[i] {
            for j in (i*i..slice.len()).step_by(i) {
                slice[j] = false;
            }
        }
    }
}

#[allow(dead_code)]
pub fn prime_sieve_is_prime(slice: & [bool], n: usize) -> bool {
	slice[n]
}
