extern crate itertools;

use std::fs::File;
use std::io::{BufRead, BufReader};
use itertools::Itertools;

fn read_file_sudoku(file_sudoku: &Vec<String>) -> [u8; 81] {
    let mut result =[0u8; 81];
    for row_i in 0..9 {
        for (i, ch) in file_sudoku[row_i].bytes().enumerate() {
            result[row_i * 9 + i] = ch - b'0';
        }
    }
    result
}

fn read_file() -> Vec<[u8; 81]>
{
    let file = File::open("p096.input").expect("Failed to open file");
    let reader = BufReader::new(file);
    let result = reader
        .lines()
        .filter_map(Result::ok)
        .chunks(10)
        .into_iter()
        .map(|chunk| chunk.skip(1).collect())
        .map(|file_sudoku| read_file_sudoku(&file_sudoku))
        .collect();
    result
}

#[test]
fn test_read_file() {
    let file_sudokus = read_file();

    let actual = file_sudokus[0];

    let expected: [u8; 81] = [
        0, 0, 3, 0, 2, 0, 6, 0, 0, 
        9, 0, 0, 3, 0, 5, 0, 0, 1, 
        0, 0, 1, 8, 0, 6, 4, 0, 0, 
        0, 0, 8, 1, 0, 2, 9, 0, 0, 
        7, 0, 0, 0, 0, 0, 0, 0, 8, 
        0, 0, 6, 7, 0, 8, 2, 0, 0, 
        0, 0, 2, 6, 0, 9, 5, 0, 0, 
        8, 0, 0, 2, 0, 3, 0, 0, 9, 
        0, 0, 5, 0, 1, 0, 3, 0, 0, 
    ];
    assert_eq!(actual, expected);
}

fn get_possible_values(sudoku: &[u8; 81], index: usize) -> [bool; 10] {
    let mut result = [true; 10];
    let row_index = index / 9;
    for v in (0..9).map(|i| sudoku[row_index * 9 + i]) {
        result[v as usize] = false;
    }
    let column_index = index % 9;
    for v in (0..9).map(|i| i * 9 + column_index).map(|i| sudoku[i]) {
        result[v as usize] = false;
    }
    let box_row_index = (row_index / 3) * 3;
    let box_column_index = (column_index / 3) * 3;
    let box_offset = box_row_index * 9 + box_column_index;
    for v in (0..9).map(|i| box_offset + (i / 3) * 9 +  (i % 3)).map(|i| sudoku[i]) {
        result[v as usize] = false;
    }
    result
}

#[test]
fn test_get_possible_values() {
    let sudoku: [u8; 81] = [
        0, 0, 3, 0, 2, 0, 6, 0, 0, 
        9, 0, 0, 3, 0, 5, 0, 0, 1, 
        0, 0, 1, 8, 0, 6, 4, 0, 0, 
        0, 0, 8, 1, 0, 2, 9, 0, 0, 
        7, 0, 0, 0, 0, 0, 0, 0, 8, 
        0, 0, 6, 7, 0, 8, 2, 0, 0, 
        0, 0, 2, 6, 0, 9, 5, 0, 0, 
        8, 0, 0, 2, 0, 3, 0, 0, 9, 
        0, 0, 5, 0, 1, 0, 3, 0, 0, 
    ];

    let left_top_actual = get_possible_values(&sudoku, 0);
    let left_top_expected = [false, false, false, false, true, true, false, false, false, false];
    assert_eq!(left_top_actual, left_top_expected);

    let right_bottom_actual = get_possible_values(&sudoku, 80);
    let right_bottom_expected = [false, false, true, false, true, false, true, true, false, false];
    assert_eq!(right_bottom_actual, right_bottom_expected);
}

fn solve_sudoku_recursive(sudoku: &mut [u8; 81], index: usize) -> bool {
    if let Some(next_empty_index) = (index..81).find(|i| sudoku[*i] == 0) {
        let possible_values = get_possible_values(sudoku, next_empty_index);
        for v in 1..=9 {
            if possible_values[v] {
                sudoku[next_empty_index] = v as u8;
                if solve_sudoku_recursive(sudoku, next_empty_index + 1) {
                    return true;
                }
            }
        }
        sudoku[next_empty_index] = 0;
        return false;
    }
    return true;
}

fn solve_sudoku(mut sudoku: [u8; 81]) -> [u8; 81] {
    solve_sudoku_recursive(&mut sudoku, 0);
    sudoku
}

#[test]
fn test_solve_sudoku() {
    let sudoku: [u8; 81] = [
        0, 0, 3, 0, 2, 0, 6, 0, 0,
        9, 0, 0, 3, 0, 5, 0, 0, 1,
        0, 0, 1, 8, 0, 6, 4, 0, 0,
        0, 0, 8, 1, 0, 2, 9, 0, 0,
        7, 0, 0, 0, 0, 0, 0, 0, 8,
        0, 0, 6, 7, 0, 8, 2, 0, 0,
        0, 0, 2, 6, 0, 9, 5, 0, 0,
        8, 0, 0, 2, 0, 3, 0, 0, 9,
        0, 0, 5, 0, 1, 0, 3, 0, 0,
    ];

    let actual = solve_sudoku(sudoku);

    let expected: [u8; 81] = [
        4, 8, 3, 9, 2, 1, 6, 5, 7,
        9, 6, 7, 3, 4, 5, 8, 2, 1,
        2, 5, 1, 8, 7, 6, 4, 9, 3,
        5, 4, 8, 1, 3, 2, 9, 7, 6,
        7, 2, 9, 5, 6, 4, 1, 3, 8,
        1, 3, 6, 7, 9, 8, 2, 4, 5,
        3, 7, 2, 6, 8, 9, 5, 1, 4,
        8, 1, 4, 2, 5, 3, 7, 6, 9,
        6, 9, 5, 4, 1, 7, 3, 8, 2];
    assert_eq!(actual, expected);
}

fn solution_number(sudoku: &[u8; 81]) -> u32 {
    let number = (0u32..3u32).map(|i| (sudoku[i as usize] as u32) * 10u32.pow(2 - i)).sum();
    number
}

#[test]
fn test_solution_number_example() {
    let solved_sudoku: [u8; 81] = [
        4, 8, 3, 9, 2, 1, 6, 5, 7,
        9, 6, 7, 3, 4, 5, 8, 2, 1,
        2, 5, 1, 8, 7, 6, 4, 9, 3,
        5, 4, 8, 1, 3, 2, 9, 7, 6,
        7, 2, 9, 5, 6, 4, 1, 3, 8,
        1, 3, 6, 7, 9, 8, 2, 4, 5,
        3, 7, 2, 6, 8, 9, 5, 1, 4,
        8, 1, 4, 2, 5, 3, 7, 6, 9,
        6, 9, 5, 4, 1, 7, 3, 8, 2];

    let actual = solution_number(&solved_sudoku);

    assert_eq!(actual, 483);
}

fn main() {
    let file_sudokus = read_file();
    let solution: u32 = file_sudokus.into_iter()
        .map(|s| solve_sudoku(s))
        .map(|s| solution_number(&s))
        .sum();
    println!("{}", solution);
}