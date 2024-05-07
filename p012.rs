mod cached_trial_division;
use cached_trial_division::CachedTrialDivision;

fn prime_factors(cache: &mut CachedTrialDivision, mut n: usize) -> Vec<usize> {    
    let square_root = (f64::sqrt(n as f64)) as usize;
    let mut result: Vec<usize> = Vec::new();
    for p in cache.get_primes(square_root) {
        if p * p > n {
            break;
        }
        while n%p == 0 {
            result.push(p);
            n /= p;
        }
    }
    if n != 1 {
        result.push(n);
    }
    result
}

#[test]
fn test_prime_factors() {
    let mut cache = CachedTrialDivision::new();
    let actual: Vec<_> = prime_factors(&mut cache, 12);
    let expected = vec![2, 2, 3];
    assert_eq!(actual, expected);
}

fn prime_factor_exponents(cache: &mut CachedTrialDivision, n: usize) -> Vec<usize> {
    let mut result: Vec<usize> = Vec::new();
    let mut exponent = 0;
    let mut previous_f = 0;
    for f in prime_factors(cache, n) {
        if f == previous_f {
            exponent += 1;
        } else {
            if exponent != 0 {
                result.push(exponent)
            }
            previous_f = f;
            exponent = 1;
        }
    }
    result.push(exponent);
    result
}

#[test]
fn test_prime_factor_exponents() {
    let mut cache = CachedTrialDivision::new();
    let actual: Vec<_> = prime_factor_exponents(&mut cache, 12);
    let expected = vec![2, 1]; // 2^2 * 3^1 == 12
    assert_eq!(actual, expected);
}

fn number_of_divisors(cache: &mut CachedTrialDivision, n: usize) -> usize {
    prime_factor_exponents(cache, n).into_iter().map(|e| e + 1).fold(1, |a, b| a * b)
}

#[test]
fn test_number_of_divisors() {
    let mut cache = CachedTrialDivision::new();
    let actual = number_of_divisors(&mut cache, 12);
    assert_eq!(actual, 6);
}

struct TriangleNumbers {
    tn: usize,
    step: usize,
}

impl Iterator for TriangleNumbers {
    type Item = usize;

    fn next(&mut self) -> Option<Self::Item> {
        let current_tn = self.tn;
        self.tn += self.step;
        self.step += 1;
        Some(current_tn)
    }
}

fn triangle_numbers() -> TriangleNumbers {
    TriangleNumbers { tn: 1, step: 2 }
}

#[test]
fn test_triangle_numbers() {
    let actual: Vec<usize> = triangle_numbers().take(10).collect();
    let expected: Vec<usize> = vec![1, 3, 6, 10, 15, 21, 28, 36, 45, 55];
    assert_eq!(actual, expected);
}

fn get_solution(minimum_number_of_divisors: usize) -> usize {
    let mut cache = CachedTrialDivision::new();
    triangle_numbers()
        .find(|&tn| number_of_divisors(&mut cache, tn) >= minimum_number_of_divisors)
        .unwrap()
}

#[test]
fn test_get_solution_example() {
    let actual = get_solution(5);
    assert_eq!(actual, 28); // 28 is the first triangle number to have over five divisors
}

fn main() {
    let solution = get_solution(500);
    println!("{}", solution);
}