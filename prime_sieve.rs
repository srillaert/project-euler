use std::iter;

pub struct BitVector {
	exclusive_upper_bound: usize,
    vector: Vec<usize>
}

impl BitVector {
    pub fn new(exclusive_upper_bound: usize) -> Self {
		let mut vector_len = exclusive_upper_bound / (usize::BITS as usize);
		if exclusive_upper_bound % (usize::BITS as usize) > 0 {
			vector_len += 1;
		}
		Self {
			exclusive_upper_bound: exclusive_upper_bound,
            vector: vec![usize::MAX; vector_len]
        }
    }

	pub fn get_nth_true_index(&self, nth: usize) -> Option<usize> {
		let mut count_ones_sum = 0usize;
		let mut index = 0;
		for i in 0..self.vector.len() {
			count_ones_sum += self.vector[i].count_ones() as usize;
			if count_ones_sum >= nth {
				index = i;
				break;
			}
		};
		for i in (0..usize::BITS).rev() {
			if ((self.vector[index] >> i) & 1) == 1 {
				if count_ones_sum == nth {
					return Some(index * usize::BITS as usize + i as usize);
				}
				count_ones_sum -= 1;
			}
		}
		return None;
	}

    pub fn get_true_indices<'a>(&'a self) -> impl Iterator<Item = usize> + 'a {
		let iterator = (0..self.exclusive_upper_bound)
			.filter_map(move |i| if self.get_value(i) { Some(i) } else { None });
		iterator
    }

	pub fn get_value(&self, nth: usize) -> bool {
		let index = nth / (usize::BITS as usize);
		let element = self.vector[index];
		let n = nth % (usize::BITS as usize);
		((element >> n) & 1) == 1
	}

	pub fn set_value(&mut self, nth: usize, value: bool) {
		let index = nth / (usize::BITS as usize);
		let n = nth % (usize::BITS as usize);
		let element = if value { self.vector[index] | (1 << n) } else { self.vector[index] & !(1 << n) };
		self.vector[index] = element;
	}
}

#[test]
fn test_new() {
	assert_eq!(BitVector::new(0).vector.len(), 0);
	assert_eq!(BitVector::new(1).vector.len(), 1);
	assert_eq!(BitVector::new(usize::BITS as usize).vector.len(), 1);
	assert_eq!(BitVector::new((usize::BITS as usize) + 1).vector.len(), 2);
}

#[test]
fn test_get_true_indices() {
	let mut bit_vector = BitVector::new(3);
	bit_vector.set_value(1, false);

	let actual: Vec<_> = bit_vector.get_true_indices().collect();

	let expected = vec![0usize, 2usize];
	assert_eq!(actual, expected);
}

#[test]
fn test_get_value() {
	let bit_vector = BitVector::new(1);
	assert!(bit_vector.get_value(0));
	assert!(bit_vector.get_value((usize::BITS as usize) - 1));
}

#[test]
fn test_set_value() {
	let mut bit_vector = BitVector::new(1);
	assert_eq!(bit_vector.vector[0].count_ones(), usize::BITS);

	bit_vector.set_value(0, false);

	assert!(!bit_vector.get_value(0));
	assert_eq!(bit_vector.vector[0].count_ones(), usize::BITS - 1);

	bit_vector.set_value(0, true);

	assert!(bit_vector.get_value(0));
	assert_eq!(bit_vector.vector[0].count_ones(), usize::BITS);
}

pub struct PrimeSieve {
    is_prime_vector: BitVector
}

impl PrimeSieve {
    pub fn new(exclusive_upper_bound: usize) -> Self {
        let vec_len = exclusive_upper_bound / 2;
        let mut is_prime = BitVector::new(vec_len);
        is_prime.set_value(0, false);
        let square_root = ((exclusive_upper_bound - 1) as f64).sqrt() as usize;
        for i in (3..=square_root).step_by(2) {
            if is_prime.get_value(i/2) {
                for j in (i*i..exclusive_upper_bound).step_by(2*i) {
                    is_prime.set_value(j/2, false);
                }
            }
        }
        Self {
            is_prime_vector: is_prime
        }
    }

	#[allow(dead_code)]
	pub fn get_nth_prime(&self, nth: usize) -> Option<usize> {
		if nth == 0 {
			return Some(2);
		}
		let element = self.is_prime_vector.get_nth_true_index(nth); // Index is 0-based, so nth(10000) gives the 10001st prime
		match element {
			Some(value) => Some(value * 2 + 1),
			None => None
		}
		//self.get_primes().nth(nth)
	}

    #[allow(dead_code)]
    pub fn get_primes<'a>(&'a self) -> impl Iterator<Item = usize> + 'a {
		let odd_primes_iterator = self.is_prime_vector.get_true_indices().map(|index| index * 2 + 1);
        iter::once(2).chain(odd_primes_iterator)
    }

    #[allow(dead_code)]
    pub fn is_prime(&self, n: usize) -> bool {
        if n%2 == 0 {
            return n == 2;
        }
        self.is_prime_vector.get_value(n/2)
    }
}

#[test]
fn test_prime_sieve_new() {
	let sieve = PrimeSieve::new(10);

	assert!(!sieve.is_prime_vector.get_value(0), "1 is not prime");
	assert!(sieve.is_prime_vector.get_value(1), "3 is prime");
	assert!(sieve.is_prime_vector.get_value(2), "5 is prime");
	assert!(sieve.is_prime_vector.get_value(3), "7 is prime");
	assert!(!sieve.is_prime_vector.get_value(4), "9 is not prime");
}

#[test]
fn test_get_nth_prime() {
	let sieve = PrimeSieve::new(1000);

	assert_eq!(sieve.get_nth_prime(0), Some(2));
	assert_eq!(sieve.get_nth_prime(1), Some(3));
	assert_eq!(sieve.get_nth_prime(166), Some(991));
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