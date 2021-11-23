def calc_operation_res(operation, num1, num2):
    if operation == 'sum':
        return (num1 + num2)
    elif operation == 'sub':
        return abs(num2 - num1)
    elif operation == 'mul':
        return (num1 * num2)


def max_common_divisor(num1, num2):
    """Return max common divisor of 2 natural numbers
    (both numbers are greater than zero)."""
    min_num = min(num1, num2)
    max_num = max(num1, num2)
    if max_num % min_num == 0:
        return min_num
    k = 2
    while k <= (min_num // 2):
        divisor = min_num // k
        if (max_num % divisor == 0) and (min_num % divisor == 0):
            return divisor
        k = k + 1
    return 1
