use std::fs::File;
use std::io::{BufReader, Read};

fn read_file(file_name: &str) -> impl Iterator<Item = u8> {
    let file = File::open(file_name).expect("Failed to open file");
    let reader = BufReader::new(file);
    let mut previous: u8 = 0;
    let numbers_in_file = reader.bytes()
        .filter_map(Result::ok)
        .filter(|&ch| ch >= b'0' && ch <= b'9')
        .map(|ch| ch - b'0')
        .enumerate()
        .filter_map(move |(i, d)| {
            if i % 2 == 0 {
                previous = d;
                None
            } else {
                Some(previous * 10 + d)
            }
        });
    numbers_in_file
}

#[test]
fn test_read_file() {
    let numbers: Vec<_> = read_file("p018.input").collect();

    assert_eq!(numbers.len(), 120); // 15 lines contain 1 + 2 + .. + 15 numbers or (15 * (15 + 1)) / 2 == 120 numbers
    assert_eq!(numbers[0], 75);
    assert_eq!(numbers[119], 23);
}

fn calculate_maximum_path_sum(mut numbers: impl Iterator<Item = u8>) -> usize {
    let mut intermediate_sum: Vec<usize> = vec![
        numbers.next().unwrap_or_default() as usize
    ];
    for row_length in 2.. {
        let Some(first_number_in_row) = numbers.next() else { break; };
        let mut previous_row_sum = intermediate_sum[0];
        intermediate_sum[0] = previous_row_sum + first_number_in_row as usize;

        for i in 1..(row_length - 1) {
            let Some(inner_number_in_row) = numbers.next() else { break; };
            let max_previous_row_sum = previous_row_sum.max(intermediate_sum[i]);
            previous_row_sum = intermediate_sum[i] as usize;
            intermediate_sum[i] = max_previous_row_sum + inner_number_in_row as usize;
        }

        let Some(last_number_in_row) = numbers.next() else { break };
        intermediate_sum.push(previous_row_sum + last_number_in_row as usize);
    }
    let result = intermediate_sum.into_iter().max().unwrap();
    result
}

#[test]
fn test_calculate_maximum_path_sum_empty() {
    let numbers: Vec<u8> = vec![];

    let actual = calculate_maximum_path_sum(numbers.into_iter());

    assert_eq!(actual, 0);
}

#[test]
fn test_calculate_maximum_path_sum_one_row() {
    let numbers: Vec<u8> = vec![
        1,
    ];

    let actual = calculate_maximum_path_sum(numbers.into_iter());

    assert_eq!(actual, 1);
}

#[test]
fn test_calculate_maximum_path_sum_two_rows() {
    let numbers: Vec<u8> = vec![
        1,
        2, 3
    ];

    let actual = calculate_maximum_path_sum(numbers.into_iter());

    assert_eq!(actual, 4);
}

#[test]
fn test_calculate_maximum_path_sum_three_rows() {
    let numbers: Vec<u8> = vec![
        1,
        2, 3,
        6, 5, 4
    ];

    let actual = calculate_maximum_path_sum(numbers.into_iter());

    assert_eq!(actual, 9);
}

pub fn get_maximum_path_sum(file_name: &str) -> usize {
    let mut numbers = read_file(file_name);
    let result = calculate_maximum_path_sum(&mut numbers);
    result
}