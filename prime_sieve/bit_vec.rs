pub struct BitVec {
	exclusive_upper_bound: usize,
	vector: Vec<usize>
}

impl BitVec {
	pub fn new(capacity: usize) -> Self {
		let mut vector_len = capacity / (usize::BITS as usize);
		if capacity % (usize::BITS as usize) > 0 {
			vector_len += 1;
		}
		Self {
			exclusive_upper_bound: capacity,
			vector: vec![usize::MAX; vector_len]
		}
	}

	pub fn get_nth_true_index(&self, nth: usize) -> Option<usize> {
		let mut count_ones_sum = 0usize;
		for (index, &word) in self.vector.iter().enumerate() {
			count_ones_sum += word.count_ones() as usize;
			if count_ones_sum >= nth {
				for i in (0..usize::BITS).rev() {
					if ((word >> i) & 1) == 1 {
						if count_ones_sum == nth {
							return Some(index * usize::BITS as usize + i as usize);
						}
						count_ones_sum -= 1;
					}
				}
			}
		}	
		None
	}

	pub fn get_true_indices<'a>(&'a self) -> impl Iterator<Item = usize> + 'a {
		let iterator = (0..self.exclusive_upper_bound)
			.filter_map(move |i| if self.get(i) { Some(i) } else { None });
		iterator
	}

	pub fn get(&self, index: usize) -> bool {
		let vector_index = index / (usize::BITS as usize);
		let word_index = index % (usize::BITS as usize);
		let word = self.vector[vector_index];
		let result = ((word >> word_index) & 1) == 1;
		result
	}

	pub fn set(&mut self, index: usize, value: bool) {
		let vector_index = index / (usize::BITS as usize);
		let word_index = index % (usize::BITS as usize);
		let word = self.vector[vector_index];
		let updated_word = if value { word | (1 << word_index) } else { word & !(1 << word_index) };
		self.vector[vector_index] = updated_word;
	}
}

#[test]
fn test_new() {
	assert_eq!(BitVec::new(0).vector.len(), 0);
	assert_eq!(BitVec::new(1).vector.len(), 1);
	assert_eq!(BitVec::new(usize::BITS as usize).vector.len(), 1);
	assert_eq!(BitVec::new((usize::BITS as usize) + 1).vector.len(), 2);
}

#[test]
fn test_get_true_indices() {
	let mut bit_vector = BitVec::new(3);
	bit_vector.set(1, false);

	let actual: Vec<_> = bit_vector.get_true_indices().collect();

	let expected = vec![0usize, 2usize];
	assert_eq!(actual, expected);
}

#[test]
fn test_get() {
	let bit_vector = BitVec::new(1);
	assert!(bit_vector.get(0));
	assert!(bit_vector.get((usize::BITS as usize) - 1));
}

#[test]
fn test_set() {
	let mut bit_vector = BitVec::new(1);
	assert_eq!(bit_vector.vector[0].count_ones(), usize::BITS);

	bit_vector.set(0, false);

	assert!(!bit_vector.get(0));
	assert_eq!(bit_vector.vector[0].count_ones(), usize::BITS - 1);

	bit_vector.set(0, true);

	assert!(bit_vector.get(0));
	assert_eq!(bit_vector.vector[0].count_ones(), usize::BITS);
}