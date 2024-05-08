const REMAINDER_TO_POSITION_NOT_SET: usize = 0;
const TILL_D: usize = 1000;

// returns the length of the recurring cyle in the decimal fraction of 1/d
// returns 0 when there is no recurring cycle
fn length_recurring_cycle(d: usize) -> usize {
    let mut remainder_to_position = [REMAINDER_TO_POSITION_NOT_SET; TILL_D];

    let mut remainder = 1;
    let mut position = 1;
    loop {
        remainder_to_position[remainder] = position;

        loop {
            remainder *= 10;
            position += 1;
            if remainder >= d {
                break;
            }
        }
        remainder = remainder % d;

        if remainder == 0 {
            return 0;
        }

        if remainder_to_position[remainder] != REMAINDER_TO_POSITION_NOT_SET {
            return position - remainder_to_position[remainder];
        }
    }
}

#[test]
fn test_length_recurring_cycle() {
    assert_eq!(length_recurring_cycle(2), 0, "1/2 = 0.5");
    assert_eq!(length_recurring_cycle(3), 1, "1/3 = 0.(3)");
    assert_eq!(length_recurring_cycle(333), 3, "1/333 = 0.(003)");
}

fn get_longest_cycle(inclusive_till: usize) -> usize {
    let mut d_longest_cycle: usize = 0;
    let mut max_length: usize = 0;
    for d in (2..=inclusive_till).rev() {
        if d <= max_length {
            break;
        }
        let length = length_recurring_cycle(d);
        if length > max_length {
            max_length = length;
            d_longest_cycle = d;
        }
    }
    d_longest_cycle
}

#[test]
fn test_get_longest_cycle_example() {
    assert_eq!(get_longest_cycle(10), 7, "1/7 has a 6-digit recurring cycle, the longest from 1/2 till 1/10")
}

fn main() {
    let solution = get_longest_cycle(TILL_D);
    println!("{}", solution);
}