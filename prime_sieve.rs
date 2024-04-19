use std::iter;

pub struct PrimeSieve {
    is_prime_slice: Vec<bool>
}

impl PrimeSieve {
    pub fn new(exclusive_upper_bound: usize) -> Self {
        let vec_len = exclusive_upper_bound / 2;
        let mut is_prime = vec![true; vec_len];
        is_prime[0] = false;
        let square_root = ((exclusive_upper_bound - 1) as f64).sqrt() as usize;
        for i in (3..=square_root).step_by(2) {            
            if is_prime[i/2] {                
                for j in (i*i..exclusive_upper_bound).step_by(2*i) {
                    is_prime[j/2] = false;
                }
            }
        }
        Self {
            is_prime_slice: is_prime
        }
    }

    #[allow(dead_code)]
    pub fn get_primes<'a>(&'a self) -> impl Iterator<Item = usize> + 'a {
        let odd_primes_iterator = self.is_prime_slice.iter().enumerate()
            .filter_map(|(index, is_prime)| if *is_prime { Some(index * 2 + 1) } else { None });
        iter::once(2).chain(odd_primes_iterator)
    }

    #[allow(dead_code)]
    pub fn is_prime(&self, n: usize) -> bool {
        if n%2 == 0 {
            return n == 2;
        }
        self.is_prime_slice[n/2]
    }
}

#[test]
fn test_new() {
    let sieve = PrimeSieve::new(10);

    let expected = vec![false, true, true, true, false];
    assert_eq!(sieve.is_prime_slice, expected);
}

#[test]
fn test_get_primes() {
    let sieve = PrimeSieve::new(20);

    let actual = sieve.get_primes().collect::<Vec<_>>();

    let expected = vec![2, 3, 5, 7, 11, 13, 17, 19];
    assert_eq!(actual, expected);
}

#[test]
fn test_is_prime() {
    let sieve = PrimeSieve::new(10);

    assert_eq!(sieve.is_prime(0), false);
    assert_eq!(sieve.is_prime(2), true);
    assert_eq!(sieve.is_prime(3), true);
    assert_eq!(sieve.is_prime(4), false);
}