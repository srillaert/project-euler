use std::fs::File;
use std::io::prelude::*;

fn read_file() -> [u8; 400] {
    let mut file = File::open("p011.input").expect("Failed to open file");
    let mut contents = String::new();
    file.read_to_string(&mut contents).expect("Failed to read file");
    let mut array = [0u8; 400];
    for (i, w) in contents.split_whitespace().enumerate() {
        array[i] = w.parse().expect("Unable to parse integer");
    }
    array
}

#[test]
fn test_read_file() {
    let numbers = read_file();
    assert_eq!(numbers.len(), 20 * 20);
    assert_eq!(numbers[0], 8); // First number
    assert_eq!(numbers[399], 48); // Last number
}

fn get_product(numbers: &[u8], start: usize, step_by: usize) -> u32 {
    let stop = start + 3 * step_by + 1;
    let index_iterator = (start..stop).step_by(step_by);
    let product = index_iterator.map(|i| numbers[i]).fold(1u32, |acc, x| acc * (x as u32));
    product
}

#[test]
fn test_get_product_horizontal() {
    let numbers = read_file();
    let result = get_product(&numbers, 0, 1);
    assert_eq!(result, 08 * 02 * 22 * 97);
}

#[test]
fn test_get_product_vertical() {
    let numbers = read_file();
    let result = get_product(&numbers, 0, 20);
    assert_eq!(result, 08 * 49 * 81 * 52);
}

fn get_maximum_product(numbers: &[u8]) -> u32 {
    const GRID_WIDTH: usize = 20;
    let mut result = 0u32;
    for i in 0..numbers.len() {
        let column = i % GRID_WIDTH;
        if column < (GRID_WIDTH - 3) {
            result = result.max(get_product(numbers, i, 1)); // horizontal right
        }
        if i < (GRID_WIDTH - 3) * GRID_WIDTH {
            result = result.max(get_product(numbers, i, GRID_WIDTH)); // vertical down
            if column >= 3 {
                result = result.max(get_product(numbers, i, GRID_WIDTH - 1)); // diagonal left down
            }
            if column < (GRID_WIDTH - 3) {
                result = result.max(get_product(numbers, i, GRID_WIDTH + 1)); // diagonal right down
            }
        }
    }
    result
}

fn main() {
    let numbers = read_file();
    let solution = get_maximum_product(&numbers);
    println!("{}", solution);
}