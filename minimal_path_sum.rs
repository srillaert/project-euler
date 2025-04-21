use std::fs::File;
use std::io::prelude::*;

pub fn read_file(file_name: &str) -> Vec<usize> {
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