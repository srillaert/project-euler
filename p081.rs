mod minimal_path_sum;
use minimal_path_sum::read_file;
use integer_sqrt::IntegerSquareRoot;

fn get_minimal_path_sum(file_name: &str) -> usize {
	let mut matrix = read_file(file_name);
	let n = matrix.len().integer_sqrt();

	for i in 1..n {
		matrix[i] += matrix[i-1];
	}
	for i in (n..matrix.len()).step_by(n) {
		matrix[i] += matrix[i-n];
		for j in (i+1)..(i+n) {
			matrix[j] += matrix[j-1].min(matrix[j-n]);
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