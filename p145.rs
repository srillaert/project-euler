fn reverse(mut n: u32) -> u32 {
	let mut result = 0;
	while n > 0 {
		result = result * 10 + n % 10;
		n /= 10;
	}
	result
}

#[test]
fn test_reverse() {
	assert_eq!(reverse(36), 63);
	assert_eq!(reverse(409), 904);
}

fn only_odd_digits(mut n: u32) -> bool {
	while n > 0 {
		if n % 2 == 0 {
			return false
		}
		n /= 10;
	}
	true
}

fn is_reversable(n: u32) -> bool {
	if n % 10 == 0 {
		return false;
	}
	let sum = n + reverse(n);
	only_odd_digits(sum)
}

#[test]
fn test_is_reversable_examples() {
	assert!(is_reversable(36));
	assert!(is_reversable(409));
}

fn get_reversable_number_count(till: u32) -> usize {
	let result = (1..till).filter(|&n| is_reversable(n)).count();
	result
}

#[test]
fn test_get_reversable_number_count_example() {
	assert_eq!(get_reversable_number_count(1000), 120);
}

fn main() {
	let solution = get_reversable_number_count(1_000_000_000);
	println!("{}", solution);
}
