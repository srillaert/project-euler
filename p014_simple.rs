fn length_collatz_sequence(n: u64) -> u16 {
    if n == 1 {
        return 1;
    } else if n % 2 == 0 {
        // n is even
        return length_collatz_sequence(n / 2) + 1;
    }
    // n is odd, then 3*n+1 is even on which we can apply immediately the next step of dividing by 2
    length_collatz_sequence((3 * n + 1) / 2) + 2
}

#[test]
fn test_length_collatz_sequence_example() {
    let actual = length_collatz_sequence(13);
    // Starting with 13 we generate the following sequence:
    // 13 to 40 to 20 to 10 to 5 to 16 to 8 to 4 to 2 to 1.
    // It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
    assert_eq!(actual, 10);
}

fn main() {
    let solution = (1..1_000_000)
        .max_by_key(|n| length_collatz_sequence(*n))
        .unwrap();
    println!("{}", solution);
}