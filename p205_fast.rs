fn convolve_distributions(distribution: Vec<f64>, sides: u32) -> Vec<f64> {
    let mut result = vec![0.0; distribution.len() + sides as usize];
    
    for (i, &p1) in distribution.iter().enumerate() {
        for (j, p2) in (0..(sides + 1)).map(|s| {
			if s == 0 {
				return 0.0;
			} else {
				1.0 / sides as f64
			}
			}).enumerate() {
            result[i + j] += p1 * p2;
        }
    }
    
    result
}

fn get_outcome_chances(sides: u32, dice: u32) -> Vec<f64> {
    // Initial distribution for one die
    let mut distribution = vec![1.0 / sides as f64; (sides + 1) as usize];
	distribution[0] = 0.0;

    // Convolve the distribution for each additional die
    for _ in 1..dice {
        distribution = convolve_distributions(distribution, sides);
    }

    distribution
}

#[test]
fn test_get_outcome_chances_one_four_sided_dice() {
	let actual: Vec<_> = get_outcome_chances(4, 1);

	let expected = vec![0.0, 0.25, 0.25, 0.25, 0.25];

	assert_eq!(actual, expected);
}

fn get_win_chance_pyramidal(pyramidal_dices_count: u32, cubic_dices_count: u32) -> f64 {
	let pyramidal_chances: Vec<_> = get_outcome_chances(4, pyramidal_dices_count);
	let cubic_chances = get_outcome_chances(6, cubic_dices_count);
	let cubic_cumulative_distribution_function: Vec<_> = 
		cubic_chances.iter()
			.scan(0.0, |state, x| {
				*state += x;
				Some(*state)
			}).collect();
	let win_chance = 
		((pyramidal_dices_count as usize)..(pyramidal_chances.len()))
		.map(|throw_outcome| cubic_cumulative_distribution_function[throw_outcome - 1] * pyramidal_chances[throw_outcome])
		.sum();
	win_chance
}

#[test]
fn test_get_win_chance_pyramidal() {
	let solution = get_win_chance_pyramidal(1, 1);
	assert_eq!(solution, 0.25);
}

fn main() {
	let solution = get_win_chance_pyramidal(9, 6);
	println!("{:.7}", solution);
}