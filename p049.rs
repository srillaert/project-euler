mod prime_sieve;
use std::collections::HashMap;

fn get_canonical_form(mut n: usize) -> usize {
    let mut digits: [usize; 4] = [0; 4];
    for i in 0..4 {
        digits[i] = n % 10;
        n /= 10;
    }
    digits.sort_unstable();
    let mut result = digits[0];
    for i in 1..4 {
        result = result * 10 + digits[i];
    }
    result
}

#[test]
fn test_get_canonical_form() {
    assert_eq!(get_canonical_form(4817), 1478)
}

fn get_arithmetic_sequences() -> Vec<(usize, usize, usize)> {
    let till = 10000;
    let sieve = prime_sieve::PrimeSieve::new(till);

    let mut permutations_hash_map: HashMap<usize, Vec<usize>> = HashMap::new();

    // Populate the permutations HashMap
    for n in 1000..till {
        if sieve.is_prime(n) {
            let key = get_canonical_form(n);
            let value = permutations_hash_map.entry(key).or_insert_with(Vec::new);
            value.push(n);
        }
    }

    // Iterate over the Permutations HashMap and find arithmetic sequences
    let mut sequences = Vec::new();
    for (_key, permutations) in permutations_hash_map {
        for (a_idx, &a) in permutations.iter().enumerate() {
            for (b_idx, &b) in permutations.iter().enumerate().skip(a_idx + 1) {
                for &c in permutations.iter().skip(b_idx + 1) {
                    if b - a == c - b {
                        sequences.push((a, b, c));
                    }
                }
            }
        }
    }

    sequences
}

#[test]
fn test_get_arithmetic_sequences() {
    // Call the get_arithmetic_sequences function and convert the result into a Vec
    let sequences = get_arithmetic_sequences();
    
    // Assert that the length of the sequences Vec is 2
    assert_eq!(sequences.len(), 2);

    // Assert that the specified triplet is in the sequences Vec
    assert!(sequences.contains(&(1487, 4817, 8147)));
}

fn main() {
    for (a, b, c) in get_arithmetic_sequences() {
        if (a, b, c) != (1487, 4817, 8147) {
            println!("{a}{b}{c}");
        }
    }
}