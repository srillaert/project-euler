fn length_collatz_sequence(memoization_array: &mut [u16], n: u64) -> u16 {
    if (n as usize) < memoization_array.len() {
        let memoization = memoization_array[n as usize];
        if memoization != 0 {
            return memoization;
        }
    }
    let length = if n % 2 == 0 {
        // n is even
        length_collatz_sequence(memoization_array, n / 2) + 1
    } else {
        // n is odd, then 3*n+1 is even on which we can apply immediately the next step of dividing by 2
        length_collatz_sequence(memoization_array, (3 * n + 1) / 2) + 2
    };
    if (n as usize) < memoization_array.len() {
        memoization_array[n as usize] = length;
    }
    length
}

#[test]
fn test_length_collatz_sequence_example() {
    let mut memoization_array = [0u16; 20];
    memoization_array[1] = 1;
    let actual = length_collatz_sequence(&mut memoization_array, 13);
    // Starting with 13 we generate the following sequence:
    // 13 to 40 to 20 to 10 to 5 to 16 to 8 to 4 to 2 to 1.
    // It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
    assert_eq!(actual, 10);
}

fn main() {
    const TILL: u64 = 1_000_000;
    let mut memoization_array = [0u16; (TILL as usize)];
    memoization_array[1] = 1;
    let solution = (1..TILL)
        .max_by_key(|n| length_collatz_sequence(&mut memoization_array, *n))
        .unwrap();
    println!("{}", solution);
}