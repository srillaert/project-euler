use integer_sqrt::IntegerSquareRoot;
use std::fs::File;
use std::io::prelude::*;

fn read_file(file_name: &str) -> Vec<usize> {
	let mut file = File::open(file_name).expect("Failed to open file");
	let mut contents = String::new();
	file.read_to_string(&mut contents).expect("Failed to read file");
	let array: Vec<usize> = contents
		.split(|c| c == ',' || c == '\n')
		.filter(|s| !s.is_empty()) // in case of trailing newlines
		.map(|w| w.parse().expect("Unable to parse integer"))
		.collect();
	array
}

fn get_minimal_path_sum(file_name: &str) -> usize {
	let mut matrix = read_file(file_name);
	let side_len = matrix.len().integer_sqrt();

	for i in 1..side_len {
		matrix[i] += matrix[i-1];
	}
	for i in (side_len..matrix.len()).step_by(side_len) {
		matrix[i] += matrix[i-side_len];
		for j in (i+1)..(i+side_len) {
			matrix[j] += matrix[j-1].min(matrix[j-side_len]);
		}
	}
	matrix[matrix.len() - 1]
}

#[test]
fn test_get_minimal_path_sum() {
	let actual = get_minimal_path_sum("p081_example.input");
	assert_eq!(actual, 2427);
}

fn main() {
	let solution = get_minimal_path_sum("p081.input");
	println!("{}", solution);
}