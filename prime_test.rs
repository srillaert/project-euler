mod prime;

#[test]
fn test_prime_sieve_initialize() {
    let mut is_prime_array = [true; 20];

    prime::prime_sieve_initialize(&mut is_prime_array);
    let actual = (1..20).filter(|&n| prime::prime_sieve_is_prime(&is_prime_array, n)).collect::<Vec<_>>();

    let expected = vec![2, 3, 5, 7, 11, 13, 17, 19];
    assert_eq!(actual, expected);
}
