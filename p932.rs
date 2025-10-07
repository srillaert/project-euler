fn is_2025_number(n: usize) -> Option<usize> {
	let square = n * n;
	let mut divisor = 10;
	while divisor < square {
		let right = square%divisor;
		if right >= (divisor / 10) {
			let sum_parts = (square/divisor) + right;
			if sum_parts == n {
				return Some(square);
			}
		}
		divisor *= 10;
	}
	return None;	
}

#[test]
fn test_is_2025_number_100() {
	assert_eq!(is_2025_number(10), None);
}

#[test]
fn test_is_2025_number_2025() {
	assert_eq!(is_2025_number(45), Some(2025));
}

fn get_2025_numbers(till: usize) -> impl Iterator<Item = usize> {
	let result = (4..till)
		.filter_map(|n| is_2025_number(n));
	result
}

#[test]
fn test_get_2025_numbers_below_square_of_10() {
	let expected = vec![81];
	assert_eq!(get_2025_numbers(10).collect::<Vec<_>>(), expected);
}

#[test]
fn test_get_2025_numbers_below_square_of_100() {
	let expected = vec![81, 2025, 3025];
	assert_eq!(get_2025_numbers(100).collect::<Vec<_>>(), expected);
}

fn get_sum_2025_numbers(till: usize) -> usize {
	return get_2025_numbers(till).sum();
}

#[test]
fn test_get_sum_2025_numbers_below_square_of_100() {
	assert_eq!(get_sum_2025_numbers(100), 5131);
}

fn main() {
	let solution = get_sum_2025_numbers(100000000);
	println!("{solution}");
}