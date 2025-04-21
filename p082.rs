mod minimal_path_sum;
use minimal_path_sum::read_file;
use integer_sqrt::IntegerSquareRoot;

fn get_minimal_path_sum(matrix: Vec<usize>) -> usize {
	let side_len = matrix.len().integer_sqrt();
	let mut minimal: Vec<_> = (0..side_len)
		.map(|i| matrix[i * side_len])
		.collect();
	for c in 1..(side_len)-1 {
		for i in 0..side_len {
			minimal[i] = minimal[i] + matrix[i * side_len + c]
		}
		for j in 1..side_len {
			minimal[j] = minimal[j].min(matrix[j * side_len + c] + minimal[j-1])
		}
		for j in (0..(side_len-1)).rev() {
			minimal[j] = minimal[j].min(matrix[j * side_len + c] + minimal[j + 1])
		}
	}
	for i in 0..side_len {
		minimal[i] = minimal[i] + matrix[i * side_len + side_len - 1]
	}
	let result = minimal.iter().min().unwrap();
	*result
}

fn get_minimal_path_sum_from_file(file_name: &str) -> usize {
	let matrix = read_file(file_name);
	let result = get_minimal_path_sum(matrix);
	result
}

#[test]
fn test_get_minimal_path_sum_down() {
	let matrix = vec![
		1,1,4,
		3,1,3,
		4,1,1
	];
	let actual = get_minimal_path_sum(matrix);
	assert_eq!(actual, 5);
}

#[test]
fn test_get_minimal_path_sum_up() {
	let matrix = vec![
		4,1,1,
		3,1,3,
		1,1,4
	];
	let actual = get_minimal_path_sum(matrix);
	assert_eq!(actual, 5);
}

#[test]
fn test_get_minimal_path_sum_from_file_example() {
	let actual = get_minimal_path_sum_from_file("p082_example.input");
	assert_eq!(actual, 994);
}

fn main() {
	let solution = get_minimal_path_sum_from_file("p082.input");
	println!("{}", solution);
}