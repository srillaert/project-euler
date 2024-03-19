fn main() {
    let till: u32 = 100;
    let sum: u32 = (1..=till).sum();
    let square_of_sum = sum * sum;
    let sum_of_squares: u32 = (1..=till).map(|i| i*i).sum();
    let solution = square_of_sum - sum_of_squares;
    println!("{}", solution);
}