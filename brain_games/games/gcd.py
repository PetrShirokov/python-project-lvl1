def max_common_divisor(num1, num2):
    """Returns the greatest common divisor of
    two positive (> 0) integer numbers."""
    min_common_divisor = 1
    min_num = min(num1, num2)
    max_num = max(num1, num2)
    if max_num % min_num == 0:
        return min_num
    supposed_result_of_division = 2
    max_result_of_division = min_num // 2
    while supposed_result_of_division <= max_result_of_division:
        divisor = min_num // supposed_result_of_division
        if (max_num % divisor == 0) and (min_num % divisor == 0):
            return divisor
        supposed_result_of_division += 1
    return min_common_divisor
