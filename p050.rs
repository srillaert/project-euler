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

fn main() {
    const TILL_SUM: usize = 1_000_000;
    let mut is_prime_array = [true; TILL_SUM];
    prime::prime_sieve_initialize(&mut is_prime_array);
    let primes = prime::prime_sieve_get_primes(& is_prime_array).collect::<Vec<_>>();

    // the prime 5 is the sum of the 2 consecutive primes 2 and 3
    let mut max_count = 2;
    let mut prime_sum = 5;

    for i in 0..primes.len() {
        if primes[i] >= TILL_SUM / max_count {
            break;
        }
        for (count, sum) in aggregate_consecutive_primes(&primes, i).take_while(|&(_, sum)| sum < TILL_SUM) {
            if count > max_count && is_prime_array[sum] {
                max_count = count;
                prime_sum = sum;
            }
        }
    }

    println!("{}", prime_sum);
}