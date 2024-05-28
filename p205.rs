fn get_outcome_counts(sides_count: u32, dices_count: u32) -> Vec<u32> {
	let highest_total = sides_count * dices_count;
	let mut result = vec![0u32; (highest_total as usize) + 1];

	for mut n in 0..(sides_count.pow(dices_count)) {
		let mut total = 0;
		for _ in 0..dices_count {
			let face_digit = (n % sides_count) + 1;
			total += face_digit;
			n = n / sides_count;
		}
		result[total as usize] += 1;
	}
	result
}

#[test]
fn test_get_outcome_counts_one_six_sided_dice() {
	let actual = get_outcome_counts(6, 1);

	let expected = vec![0, 1, 1, 1, 1, 1, 1];

	assert_eq!(actual, expected);
}

#[test]
fn test_get_outcome_counts_one_four_sided_dice() {
	let actual = get_outcome_counts(4, 1);

	let expected = vec![0, 1, 1, 1, 1];

	assert_eq!(actual, expected);
}

#[test]
fn test_get_outcome_counts_two_four_sided_dice() {
	let actual = get_outcome_counts(4, 2);

	let expected = vec![0, 0, 1, 2, 3, 4, 3, 2, 1];

	assert_eq!(actual, expected);
}

#[test]
fn test_get_outcome_counts_nine_four_sided_dice() {
	let actual = get_outcome_counts(4, 9);

	assert_eq!(37, actual.len());
	let sum_counts: u32 = actual.iter().sum();
	assert_eq!(4u32.pow(9), sum_counts);
	assert_eq!(1, actual[9]);
	assert_eq!(9, actual[10]);
	assert_eq!(9, actual[35]);
	assert_eq!(1, actual[36]);
}

fn get_outcome_chances(sides_count: u32, dices_count: u32) -> Vec<f64> {
	let counts = get_outcome_counts(sides_count, dices_count);
	let sum: u32 = counts.iter().sum();
	let chances = counts.iter().map(|&c| (c as f64) / sum as f64).collect();
	chances
}

#[test]
fn test_get_outcome_chances_one_four_sided_dice() {
	let actual = get_outcome_chances(4, 1);

	let expected = vec![0.0, 0.25, 0.25, 0.25, 0.25];

	assert_eq!(actual, expected);
}

fn get_solution(pyramidal_dices_count: u32, cubic_dices_count: u32) -> f64 {
	let pyramidal_chances = get_outcome_chances(4, pyramidal_dices_count);
	let cubic_chances = get_outcome_chances(6, cubic_dices_count);
	let mut win_chance = 0.0;
	for total in (pyramidal_dices_count as usize)..(pyramidal_chances.len()) {
		let win_chance_for_total: f64 = (0..total).map(|i| cubic_chances[i]).sum();
		let pyramidal_chance_for_total = pyramidal_chances[total];
		win_chance += pyramidal_chance_for_total * win_chance_for_total;
	}
	win_chance
}

#[test]
fn test_get_solution() {
	let solution = get_solution(1, 1);
	assert_eq!(solution, 0.25);
}

fn main() {
	let solution = get_solution(9, 6);
	println!("{:.7}", solution);
}