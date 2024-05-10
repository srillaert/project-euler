use std::cmp::max;
use std::fs::File;
use std::io::{BufReader, Read};

fn read_file(file_name: &str) -> Vec<u8> {
    let file = File::open(file_name).expect("Failed to open file");
    let reader = BufReader::new(file);

    let digits_in_file = reader.bytes()
        .filter_map(Result::ok)
        .filter(|&ch| ch >= b'0' && ch <= b'9')
        .map(|ch| ch - b'0');
    
    let mut result: Vec<u8> = Vec::<_>::new();
    let mut iterator = digits_in_file.into_iter();
    loop {
        let Some(first_digit) = iterator.next() else { break; };
        let Some(second_digit) = iterator.next() else { break; };
        let number = first_digit * 10 + second_digit;
        result.push(number);
    }
    result
}

#[test]
fn test_read_file() {
    let numbers = read_file("p018.input");

    assert_eq!(numbers.len(), 120); // 15 lines contain 1 + 2 + .. + 15 numbers or (15 * (15 + 1)) / 2 == 120 numbers
    assert_eq!(numbers[0], 75);
    assert_eq!(numbers[119], 23);
}

fn get_row_count(triangular_number: usize) -> usize {
    let discriminant = 1 + 8 * triangular_number;
    let sqrt_discriminant = (discriminant as f64).sqrt() as usize;
    (sqrt_discriminant - 1) / 2
}

#[test]
fn test_get_row_count() {
    assert_eq!(get_row_count(120), 15); // 15 lines contain 1 + 2 + .. + 15 numbers or (15 * (15 + 1)) / 2 == 120 numbers
    assert_eq!(get_row_count(3), 2);
}

fn calculate_maximum_path_sum(numbers: &Vec<u8>) -> usize {
    let row_count = get_row_count(numbers.len());
    let mut maximum_path_row: Vec<_> = ((numbers.len() - row_count).. numbers.len()).map(|i| numbers[i] as usize).collect();
    for row_index in (0..(row_count - 1)).rev() {
        for column_index in 0..=row_index {
            let row_start = ((row_index) * (row_index + 1)) / 2;
            maximum_path_row[column_index] = 
                numbers[row_start + column_index] as usize + 
                max(maximum_path_row[column_index],
                    maximum_path_row[column_index + 1]);
        }
    }
    maximum_path_row[0]
}

#[test]
fn test_calculate_maximum_path_sum() {
    let numbers: Vec<u8> = vec![
        1,
        2, 3
    ];

    let actual = calculate_maximum_path_sum(&numbers);

    assert_eq!(actual, 4);
}

pub fn get_maximum_path_sum(file_name: &str) -> usize {
    let numbers = read_file(file_name);
    let result = calculate_maximum_path_sum(&numbers);
    result
}