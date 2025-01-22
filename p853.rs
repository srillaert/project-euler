fn is_pisano_period_equal(n: usize, expected_pisano_period: usize) -> bool {
	let start = (0usize, 1usize);
	let mut current = start;
	for counter in 1..=expected_pisano_period {
		current = (current.1, (current.0 + current.1) % n);
		if current == start {
			return counter == expected_pisano_period;
		}
	}
	false
}

#[test]
fn test_is_pisano_period_equal() {
	assert!(is_pisano_period_equal(3, 8));

	assert!(!is_pisano_period_equal(18, 18));
	assert!(is_pisano_period_equal(19, 18)); // pisano_period(19) == 18
	assert!(!is_pisano_period_equal(20, 18));
}

fn sum_values(expected_pisano_period: usize, n_till: usize) -> usize {
	(3..n_till).filter(|&n| is_pisano_period_equal(n, expected_pisano_period)).sum()
}

#[test]
fn test_sum_values() {
	assert_eq!(sum_values(18, 50), 57);
}

fn main() {
	let solution = sum_values(120, 1_000_000_000);
	println!("{solution}");
}