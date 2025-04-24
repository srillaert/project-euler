mod minimal_path_sum;
use integer_sqrt::IntegerSquareRoot;
use minimal_path_sum::read_file;
use std::cmp::Reverse;
use std::collections::BinaryHeap;

fn get_minimal_path_sum(matrix: &[usize]) -> usize {
	let n = matrix.len().integer_sqrt();
	let mut dist = vec![usize::MAX; matrix.len()];
	let mut heap: BinaryHeap<(Reverse<usize>, usize, usize)> = BinaryHeap::new();
	heap.push((Reverse(matrix[0]), 0, 0));
	let directions: [(isize, isize); 4] = [
		( 1,  0),
		(-1,  0),
		( 0,  1),
		( 0, -1),
	];
	while let Some((Reverse(cost), x, y)) = heap.pop() {
		for &(dx, dy) in &directions {
			let nx_i = x as isize + dx;
			let ny_i = y as isize + dy;
			if (0..n as isize).contains(&nx_i) && (0..n as isize).contains(&ny_i) {
				let nx = nx_i as usize;
				let ny = ny_i as usize;
				let ni = ny * n + nx;
				let ncost = cost + matrix[ni];
				if ncost < dist[ni] {
					dist[ni] = ncost;
					heap.push((Reverse(ncost), nx, ny));
				}
			}
		}
	}
	dist[dist.len()-1]
}

fn get_minimal_path_sum_from_file(file_name: &str) -> usize {
	let matrix = read_file(file_name);
	let result = get_minimal_path_sum(&matrix);
	result
}

#[test]
fn test_get_minimal_path_sum_from_file_example() {
	let actual = get_minimal_path_sum_from_file("p083_example.input");
	assert_eq!(actual, 2297);
}

fn main() {
	let solution = get_minimal_path_sum_from_file("p083.input");
	println!("{}", solution);
}