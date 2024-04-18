pub struct PrimeSieve {
    is_prime_slice: Vec<bool>
}

impl PrimeSieve {
    pub fn new(exclusive_upper_bound: usize) -> Self {
        let mut is_prime = vec![true; exclusive_upper_bound];
        is_prime[0] = false;
        is_prime[1] = false;
        let square_root = ((exclusive_upper_bound - 1) as f64).sqrt() as usize;
        for i in 0..=square_root {
            if is_prime[i] {
                for j in (i*i..exclusive_upper_bound).step_by(i) {
                    is_prime[j] = false;
                }
            }
        }
        Self {
            is_prime_slice: is_prime
        }
    }

    pub fn get_primes<'a>(&'a self) -> impl Iterator<Item = usize> + 'a {
        (2..self.is_prime_slice.len()).filter(move |&n| self.is_prime(n))
    }

    pub fn is_prime(&self, n: usize) -> bool {
        self.is_prime_slice[n]
    }
}

#[test]
fn test_is_prime() {
    let sieve = PrimeSieve::new(10);

    assert_eq!(sieve.is_prime(0), false);
    assert_eq!(sieve.is_prime(2), true);
}

#[test]
fn test_get_primes() {
    let sieve = PrimeSieve::new(20);

    let actual = sieve.get_primes().collect::<Vec<_>>();

    let expected = vec![2, 3, 5, 7, 11, 13, 17, 19];
    assert_eq!(actual, expected);
}
