fn get_least_common_multiple() -> u32 {
    // On how to initialize a Rust array with increasing values : https://stackoverflow.com/questions/36925673/how-can-i-initialize-an-array-using-a-function
    let mut array: [u8; 21] = core::array::from_fn(|i| i as u8);
    let mut result: u32 = 1;
    for i in 2..=20 {
        result *= array[i] as u32;
        for j in (2*i..=20).step_by(i) {
            array[j] /= array[i];
        }
    }
    result
}

fn main() {
    let solution = get_least_common_multiple();
    println!("{solution}");
}