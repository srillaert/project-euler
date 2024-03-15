fn main() {
    let (mut former, mut latter) = (0, 1);
    let mut sum = 0;
    while latter <= 4_000_000 {
        if latter % 2 == 0 {
            sum += latter;
        }
        (former, latter) = (latter, former + latter);
    }
    println!("{sum}");
}