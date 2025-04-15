mod prime_sieve;
use integer_sqrt::IntegerSquareRoot;
use itertools::Itertools;

fn get_factors_doubling_divisors(sieve_till: usize, number_factors: usize) -> impl Iterator<Item = usize> {
	let sieve = prime_sieve::PrimeSieve::new(sieve_till);
	let primes= sieve.get_primes().take(number_factors).collect::<Vec<_>>();
	let largest_prime = primes[primes.len() - 1];
	let sqrt_largest_prime = largest_prime.integer_sqrt();
	let primes_power_2n = primes
		.iter()
		.take_while(|&p| *p <= sqrt_largest_prime)
		.flat_map(|p| {
			let mut square: usize = *p;
			std::iter::from_fn(move || {
				square = square * square;
				if square < largest_prime {
					Some(square)
				} else {
					None
				}
			})
		})
		.sorted();
	let factors = primes.into_iter().merge(primes_power_2n).take(number_factors);
	factors
}

#[test]
fn test_get_factors_doubling_divisors() {
	assert_eq!(get_factors_doubling_divisors(100, 9).collect::<Vec<_>>(), [2, 3, 4, 5, 7, 9, 11, 13, 16]);
}

fn get_smallest_number_with_power_of_2_divisors(sieve_till: usize, number_factors: usize) -> usize {
	let result = get_factors_doubling_divisors(sieve_till, number_factors).reduce(|acc, num| (acc * num) % 500_500_507).unwrap();
	result
}

#[test]
fn test_get_smallest_number_with_power_of_2_divisors() {
	assert_eq!(get_smallest_number_with_power_of_2_divisors(100, 6), 7560)
}

fn main() {
	let solution = get_smallest_number_with_power_of_2_divisors(8_000_000, 500_500);
	println!("{solution}");
}