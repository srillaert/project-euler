use std::fs::File;
use std::io::{BufReader, Read};
use std::path::Path;

fn get_max_product_vector(digits: Vec<u8>, length: usize) -> u64 {
    digits.windows(length)
        .map(|window| window.iter().map(|&d| d as u64).product())
        .max()
        .unwrap()
}

#[test]
fn test_get_max_product_vector_at_end() {
    let digits = (0..4).into_iter().collect();
    let result = get_max_product_vector(digits, 2);
    assert_eq!(result, 2 * 3);
}

#[test]
fn test_get_max_product_vector_at_start() {
    let digits = (0..4).into_iter().rev().collect();
    let result = get_max_product_vector(digits, 2);
    assert_eq!(result, 3 * 2);
}

fn get_digits_from_file() -> Vec<u8> {
    let path = Path::new("p008.input");
    let file = File::open(&path).expect("Failed to open file");
    let mut reader = BufReader::new(file);
    let mut contents = String::new();
    reader.read_to_string(&mut contents).expect("Failed to read file");

    let digits: Vec<u8> = contents
        .chars()
        .filter(|c| c.is_digit(10))
        .map(|c| c.to_digit(10).unwrap() as u8)
        .collect();

    digits
}

#[test]
fn test_get_digits_from_file() {
    let digits = get_digits_from_file();
    assert_eq!(digits.len(), 1000); // problem description: file contains 1000 digit number
}

fn get_max_product_file(length: usize) -> u64 {
    let digits = get_digits_from_file();
    let max_product = get_max_product_vector(digits, length);
    max_product
}

#[test]
fn test_get_max_product_file_example() {
    let result = get_max_product_file(4);
    assert_eq!(result, 5832);
}

fn main() {
    let solution = get_max_product_file(13);
    println!("{}", solution);
}