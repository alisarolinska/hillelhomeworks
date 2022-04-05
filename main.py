def calculate (digit_A, digit_B, op_type):
    if op_type == "+" :
        return digit_A + digit_B
    if op_type == "-" :
        return digit_A - digit_B
    if op_type == "*" :
        return digit_A * digit_B
    if op_type == "/":
        return digit_A / digit_B


print(calculate(93, 4, '*'))
