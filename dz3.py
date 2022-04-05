def sum_range(x, y):
    if x == y:
        return x
    if x < y:
        return sum(range(x, y+1))
    if x > y:
        return sum(range(y, x+1))


print(sum_range(12, 19))