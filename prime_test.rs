mod prime;

#[test]
fn test_prime_sieve_get_primes() {
    let mut is_prime_array = [true; 20];

    prime::prime_sieve_initialize(&mut is_prime_array);
    let actual = prime::prime_sieve_get_primes(&is_prime_array).collect::<Vec<_>>();

    let expected = vec![2, 3, 5, 7, 11, 13, 17, 19];
    assert_eq!(actual, expected);
}
