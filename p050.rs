mod prime_sieve;

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
pub fn get_solution(exclusive_upper_bound: usize) -> usize {
    let sieve = prime_sieve::PrimeSieve::new(exclusive_upper_bound);
    let primes = sieve.get_primes().collect::<Vec<_>>();

    // the prime 5 is the sum of the 2 consecutive primes 2 and 3
    let mut max_count = 2;
    let mut prime_sum = 5;

    for i in 0..primes.len() {
        if primes[i] >= exclusive_upper_bound / max_count {
            break;
        }
        for (count, sum) in aggregate_consecutive_primes(&primes, i).take_while(|&(_, sum)| sum < exclusive_upper_bound) {
            if count > max_count && sieve.is_prime(sum) {
                max_count = count;
                prime_sum = sum;
            }
        }
    }
    prime_sum
}

#[test]
fn test_get_solution_examples() {
    assert_eq!(get_solution(100), 41);
    assert_eq!(get_solution(1000), 953)
}

fn main() {
    let prime_sum = get_solution(1_000_000);
    println!("{}", prime_sum);
}