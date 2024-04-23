mod cached_trial_division;

fn main() {
    let mut cache = cached_trial_division::CachedTrialDivision::new();
    let mut primes_count = 0;
    let mut ulam_spiral_index = 1;
    let solution = loop {
        let side_length = 2 * ulam_spiral_index + 1;
        let bottom_right_corner = side_length * side_length;
        let current_add = 2 * ulam_spiral_index;
        let extra_primes_count = (1..4)
            .filter(|&corner_index| cache.is_prime(bottom_right_corner - corner_index * current_add))
            .count();
        primes_count += extra_primes_count;
        let numbers_count = 1 + 4 * ulam_spiral_index;
        if (primes_count * 100 / numbers_count) < 10 {
            break side_length;
        }
        ulam_spiral_index = ulam_spiral_index + 1;
    };
    println!("{}", solution);
}