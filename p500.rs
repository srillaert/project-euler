mod prime_sieve;
use itertools::Itertools;

fn get_factors<'a>(sieve_till: usize, number_factors: usize) -> impl Iterator<Item = usize> + 'a {
	let sieve = prime_sieve::PrimeSieve::new(sieve_till);
	let primes= sieve.get_primes().take(number_factors).collect::<Vec<_>>();
	let largest_prime = primes[primes.len() - 1];
	let squareroot_largest_prime = (largest_prime as f64).sqrt() as usize;
	let mut squared_primes = primes
		.iter()
		.take_while(|&p| *p <= squareroot_largest_prime)
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
		.collect::<Vec<_>>();
	squared_primes.sort();
	let factors = primes.into_iter().merge(squared_primes).take(number_factors);
	return factors;
}

#[test]
fn test_get_factors() {
	assert_eq!(get_factors(100, 7).collect::<Vec<_>>(), [2, 3, 4, 5, 7, 9, 11]);
}

fn get_smallest_number_with_power_of_2_divisors(sieve_till: usize, number_factors: usize) -> usize {
	let result = get_factors(sieve_till, number_factors).reduce(|acc, num| (acc * num) % 500_500_507).unwrap();
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