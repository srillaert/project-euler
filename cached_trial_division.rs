pub struct CachedTrialDivision {
    cached_primes: Vec<usize>,
}

impl CachedTrialDivision {
    pub fn new() -> Self {
        Self {
            cached_primes: vec![2, 3],
        }
    }

    #[allow(dead_code)]
    fn is_prime_limited(&self, n: usize, square_root_n: usize) -> bool {
        for i in 0..self.cached_primes.len() {
            let p = self.cached_primes[i];
            if p > square_root_n {
                return true;
            }
            if n % p == 0 {
                return false;
            }
        }
        return true;
    }

    #[allow(dead_code)]
    fn expand_cached_primes(&mut self, inclusive_till: usize) {
        let last_prime = self.cached_primes[self.cached_primes.len() - 1];
        let mut n = last_prime + 2;
        loop {
            let square_root_n = f64::sqrt(n as f64) as usize;
            let is_prime = self.is_prime_limited(n, square_root_n);
            if is_prime {
                self.cached_primes.push(n);
                if n > inclusive_till {
                    return;
                }
            }
            n = n + 2;
        }
    }

    fn conditionally_expand_cached_primes(&mut self, inclusive_till: usize) {
        let last_prime = self.cached_primes[self.cached_primes.len() - 1];
        if last_prime < inclusive_till {
            self.expand_cached_primes(inclusive_till);
        }
    }

    #[allow(dead_code)]
    pub fn get_primes(&mut self, inclusive_till: usize) -> impl Iterator<Item= usize> {
        self.conditionally_expand_cached_primes(inclusive_till);
        self.cached_primes.clone().into_iter().take_while(move |&p| p <= inclusive_till)
    }

    #[allow(dead_code)]
    pub fn is_prime(&mut self, n: usize) -> bool {
        let square_root_n = f64::sqrt(n as f64) as usize;
        self.conditionally_expand_cached_primes(square_root_n);
        return self.is_prime_limited(n, square_root_n);
    }
}

#[test]
fn test_get_primes() {
    let mut cache = CachedTrialDivision::new();

    let actual: Vec<_> = cache.get_primes(11).collect();

    let expected: Vec<_> = vec![2, 3, 5, 7, 11];
    assert_eq!(actual, expected)
}

#[test]
fn test_is_prime() {
    let mut cache = CachedTrialDivision::new();

    assert_eq!(cache.is_prime(2), true);
    assert_eq!(cache.is_prime(3), true);
    assert_eq!(cache.is_prime(4), false);
    assert_eq!(cache.is_prime(9), false);
    assert_eq!(cache.is_prime(25), false);
}