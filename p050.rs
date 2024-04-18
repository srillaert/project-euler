mod prime;

fn aggregate_consecutive_primes(primes: &[usize], i: usize) -> impl Iterator<Item = (usize, usize)> + '_ {
    let mut sum = 0;
    let mut count = 0;    
    primes[i..].iter().map(move |&prime| {
        sum += prime;
        count += 1;
        (count, sum)
    })
}

// Find the biggest prime less than is_prime_array.len() that is the sum of the most consecutive primes
pub fn get_solution(is_prime_array: &mut [bool]) -> usize {
    prime::prime_sieve_initialize(is_prime_array);
    let primes = prime::prime_sieve_get_primes(& is_prime_array).collect::<Vec<_>>();

    // the prime 5 is the sum of the 2 consecutive primes 2 and 3
    let mut max_count = 2;
    let mut prime_sum = 5;

    for i in 0..primes.len() {
        if primes[i] >= is_prime_array.len() / max_count {
            break;
        }
        for (count, sum) in aggregate_consecutive_primes(&primes, i).take_while(|&(_, sum)| sum < is_prime_array.len()) {
            if count > max_count && is_prime_array[sum] {
                max_count = count;
                prime_sum = sum;
            }
        }
    }
    prime_sum
}

#[test]
fn test_get_solution_examples() {
    let mut hundred_array = [true; 100];
    assert_eq!(get_solution(&mut hundred_array), 41);

    let mut thousand_array = [true; 1000];
    assert_eq!(get_solution(&mut thousand_array), 953)
}

fn main() {
    let mut is_prime_array = [true; 1_000_000];
    let prime_sum = get_solution(&mut is_prime_array);
    println!("{}", prime_sum);
}