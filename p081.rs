mod minimal_path_sum;
use minimal_path_sum::read_file;
use integer_sqrt::IntegerSquareRoot;

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