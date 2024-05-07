pub struct TriangleNumbers {
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

pub fn triangle_numbers() -> TriangleNumbers {
    TriangleNumbers { tn: 1, step: 2 }
}

#[test]
fn test_triangle_numbers() {
    let actual: Vec<usize> = triangle_numbers().take(10).collect();
    let expected: Vec<usize> = vec![1, 3, 6, 10, 15, 21, 28, 36, 45, 55];
    assert_eq!(actual, expected);
}