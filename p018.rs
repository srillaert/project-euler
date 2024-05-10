use std::cmp::max;
use std::fs::File;
use std::io::{BufReader, Read};

fn read_file() -> Vec<u16> {
    let file = File::open("p018.input").expect("Failed to open file");
    let reader = BufReader::new(file);

    let digits_in_file = reader.bytes()
        .filter_map(Result::ok)
        .filter(|&ch| ch >= b'0' && ch <= b'9')
        .map(|ch| ch - b'0');
    
    let mut result: Vec<u16> = Vec::<_>::new();
    let mut iterator = digits_in_file.into_iter();
    loop {
        let Some(first_digit) = iterator.next() else { break; };
        let Some(second_digit) = iterator.next() else { break; };
        let number = first_digit * 10 + second_digit;
        result.push(number.into());
    }
    result
}

#[test]
fn test_read_file() {
    let numbers = read_file();

    assert_eq!(numbers.len(), 120); // 15 lines contain 1 + 2 + .. + 15 numbers or (15 * (15 + 1)) / 2 == 120 numbers
    assert_eq!(numbers[0], 75);
    assert_eq!(numbers[119], 23);
}

fn get_maximum_path_sum(numbers: &mut Vec<u16>, row_count: usize) -> u16 {
    for row_index in (0..(row_count - 1)).rev() {
        for column_index in 0..(row_index + 1) {
            let row_start = ((row_index) * (row_index + 1)) / 2;
            let next_row_start = row_start + (row_index + 1);
            numbers[row_start + column_index] += 
                max(numbers[next_row_start + column_index],
                    numbers[next_row_start + column_index + 1]);
        }
    }
    numbers[0]
}

#[test]
fn test_get_maximum_path_sum() {
    let mut numbers: Vec<u16> = vec![
        1,
        2, 3
    ];

    let actual = get_maximum_path_sum(&mut numbers, 2);

    assert_eq!(actual, 4);
}

fn main() {
    let mut numbers = read_file();
    let solution = get_maximum_path_sum(&mut numbers, 15);
    println!("{}", solution);
}