def calculate (digit_A, digit_B, op_type):
    if op_type == "+" :
        return digit_A + digit_B
    if op_type == "-" :
        return digit_A - digit_B
    if op_type == "*" :
        return digit_A * digit_B
    if op_type == "/":
        if digit_B == 0:
            print("На ноль делить нельзя")
        else:
            return digit_A / digit_B




print(calculate(15.48, 50, '*'))
print(calculate(93, 0, '/'))