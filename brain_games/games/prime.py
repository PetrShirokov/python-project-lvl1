def is_prime(num: int):
    """Return 'yes' if num is prime, and 'no' if it's not.
    Num is natural and greater or equal two."""
    if num == 2:
        is_prime_str = 'yes'
    upper_range_bound = (num // 2) + 1
    for i in range(2, upper_range_bound):
        expected_divisor = num // i
        if num % expected_divisor == 0:
            is_prime_str = 'no'
            return is_prime_str
    is_prime_str = 'yes'
    return is_prime_str
