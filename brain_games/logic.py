def calc_operation_res(operation, num1, num2):
    if operation == 'sum':
        return (num1 + num2)
    elif operation == 'sub':
        return abs(num2 - num1)
    elif operation == 'mul':
        return (num1 * num2)
