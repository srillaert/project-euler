mod prime_sieve;

fn get_number_hybrid_integers(base: usize, exponent: usize) -> usize {
	let ln_till = (exponent as f64) * (base as f64).ln();
	let sieve_till = ((exponent as f64) * (base as f64).log2()) as usize;
	let sieve = prime_sieve::PrimeSieve::new(sieve_till);
	let primes = sieve.get_primes().collect::<Vec<_>>();
	let mut count = 0usize;
	for (i, p) in primes.iter().enumerate() {
		let ln_p = (*p as f64).ln();
		if 2f64 * (*p as f64) * ln_p >= ln_till {
			break;
		}
		// Use binary search to find the first prime q where p**q * q**p > base**exponent
		// Can probably be replaced by Rust slice binary_search_by
		let mut low = i + 1;
		let mut high = primes.len();
		while low < high {
			let mid = (low + high) / 2;
			let q = primes[mid] as f64;
			let ln_hybrid_integer = q * ln_p + (*p as f64) * q.ln();
			if ln_hybrid_integer > ln_till + 1e-9 {
				high = mid;
			} else {
				low = mid + 1;
			}
		}
		count += low - (i + 1);
	}
	return count;
}

#[test]
fn test_get_number_hybrid_integers() {
	let first_ordered_hybrid_integers: [usize; 5] = [
		72, // 2**3 * 3**2
		800, // 2**5 * 5**2
		6272, // 2**7 * 7**2
		30375, // 3**5 * 5**3
		247808, // 2**11 * 11**2
	];
	for (i, hi) in first_ordered_hybrid_integers.iter().enumerate() {
		assert_eq!(get_number_hybrid_integers(*hi - 1, 1), i);
		assert_eq!(get_number_hybrid_integers(*hi, 1), i + 1);
	}
}

#[test]
fn test_solution_examples() {
	assert_eq!(get_number_hybrid_integers(800, 1), 2);
	assert_eq!(get_number_hybrid_integers(800, 800), 10790);
}

fn main() {
	let solution = get_number_hybrid_integers(800800, 800800);
	println!("{}", solution);
}