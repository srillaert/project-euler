use std::fs::File;
use std::io::{BufReader, Read};

fn read_file() -> Vec<u8> {    
    let file = File::open("p013.input").expect("Failed to open file");
    let reader = BufReader::new(file);
    let mut digits: Vec<u8> = Vec::new();
    for result in reader.bytes() {
        let character = result.unwrap();
        if character != b'\n' {
            digits.push(character - b'0')
        }
    }
    digits
}

fn sum_digits(digits: Vec<u8>) -> Vec<u16> {
    let mut sum: Vec<u16> = vec![0u16; 52];
    for i in 0..digits.len() {
        let sum_index = 49- (i % 50);
        sum[sum_index] += digits[i] as u16;
    }
    for i in 0..sum.len() {
        let carry = sum[i] / 10;
        sum[i] = sum[i] % 10;
        if carry > 0 {
            sum[i + 1] += carry;
        }
    }
    sum
}

#[test]
fn test_read_file() {
    let digits = read_file();
    assert_eq!(digits.len(), 5000);
}

fn main() {
    let digits = read_file();
    let sum = sum_digits(digits);
    for i in 0..10 {
        print!("{}", sum[sum.len() - i - 1]);
    }
    println!();
}