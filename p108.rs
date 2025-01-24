fn get_distinct_solutions(n: usize) -> impl Iterator<Item = (usize, usize)> {
	let result = ((n+1)..=(2*n))
		.filter(move |&x| x*n % (x-n) == 0)
		.map(move |x| (x, x*n / (x-n)));
	result
}

#[test]
fn test_get_distinct_solutions_example() {
	let expected = vec![(5, 20), (6, 12), (8, 8)];
	assert_eq!(get_distinct_solutions(4).collect::<Vec<_>>(), expected);
}

fn main() {
	let solution = (1000..200000)
		.find(|&n| get_distinct_solutions(n).count() > 1000)
		.unwrap();
	println!("{solution}");
}