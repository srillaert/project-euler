mod cached_trial_division;
use cached_trial_division::CachedTrialDivision;

fn number_of_divisors(cache: &mut CachedTrialDivision, mut n: usize) -> usize {
    let square_root = (f64::sqrt(n as f64)) as usize;
    let mut result = 1usize;
    for p in cache.get_primes(square_root) {
        if p * p > n {
            break;
        }
        if n%p == 0 {
            let mut exponent = 0;
            while n%p == 0 {
                exponent += 1;
                n /= p;
            }
            result *= exponent + 1;
        }
    }
    if n != 1 {
        result *= 2;
    }
    result
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