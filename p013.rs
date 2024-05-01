use std::fs::File;
use std::io::{BufReader, Read};

fn read_file() -> impl Iterator<Item = (usize, u8)> {    
    let file = File::open("p013.input").expect("Failed to open file");
    let reader = BufReader::new(file);
    reader.bytes()
        .filter_map(Result::ok)
        .filter(|&ch| ch != b'\n')
        .enumerate()
        .map(|(i, ch)| (49 - (i%50), ch - b'0'))
}

#[test]
fn test_read_file() {
    let digits: Vec<_> = read_file().collect();
    assert_eq!(digits.len(), 5000);
    assert_eq!(digits[0], (49, 3)); // first digit in file is 3
    assert_eq!(digits[4999], (0, 0)); // last digit in file is 0
}

fn main() {
    let mut sum: [u16; 52] = [0u16; 52];
    for (index, digit) in read_file() {
        sum[index] += digit as u16;
    }

    let mut carry = 0;
    for digit in sum.iter_mut() {
        *digit += carry;
        carry = *digit / 10;
        *digit %= 10;
    }

    for digit in sum.iter().rev().take(10) {
        print!("{}", digit);
    }
    println!();
}