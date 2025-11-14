fn calculate_p(l: usize, mut n: usize) -> usize {
	let power_of_10 = 10f64.powf((l as f64).log10().floor());
	let base_l = (l as f64) / power_of_10;
	let min = base_l.log10();
	let max = (base_l + 1f64 / power_of_10).log10();
	let log10_of_2 = 2f64.log10();
	let mut digits_log = log10_of_2;
	let mut power = 1usize;
	loop {
		if digits_log >= min && digits_log < max {
			n -= 1;
			if n == 0 {
				return power;
			}
		}
		power += 1usize;
		digits_log = (digits_log + log10_of_2) % 1f64;
	}
}

#[test]
fn test_calculate_p_examples() {
	assert_eq!(calculate_p(12, 1), 7);
	assert_eq!(calculate_p(12, 2), 80);
	assert_eq!(calculate_p(123, 45), 12710);
}

fn main() {
	let solution = calculate_p(123, 678910);
	println!("{solution}");
}