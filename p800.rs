mod prime_sieve;

/// Calculates the number of hybrid integers less than or equal to base^exponent.
fn get_number_hybrid_integers(base: usize, exponent: usize) -> usize {
	let ln_till = (exponent as f64) * (base as f64).ln();
	let sieve_till = ((exponent as f64) * (base as f64).log2()) as usize;
	let sieve = prime_sieve::PrimeSieve::new(sieve_till);
	let primes = sieve.get_primes().collect::<Vec<_>>();
	let mut count = 0usize;
	for (p_i, p) in primes.iter().enumerate() {
		let p_as_f64 = *p as f64;
		let ln_p = p_as_f64.ln();
		if 2f64 * p_as_f64 * ln_p >= ln_till {
			break;
		}
		// Use binary search to the number of q's greater than p where p^q * q^p <= base^exponent
		let count_for_p = primes[p_i + 1..]
			.binary_search_by(|&q| {
				let q_as_f64 = q as f64;
				let ln_hybrid_integer = q_as_f64 * ln_p + p_as_f64 * q_as_f64.ln();
				if ln_hybrid_integer > ln_till {
					std::cmp::Ordering::Greater
				} else {
					std::cmp::Ordering::Less
				}
			})
		.unwrap_or_else(|x| x);
		count += count_for_p;
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