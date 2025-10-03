def least_squares(x, y):
    n = len(x)

    sum_x = sum(x)
    sum_y = sum(y)
    sum_xy = sum(x_i * y_i for x_i, y_i in zip(x, y))
    sum_x2 = sum(x_i**2 for x_i in x)

    denom = n * sum_x2 - sum_x**2

    b = (n * sum_xy - sum_x * sum_y) / denom
    a = (sum_y - b * sum_x) / n

    return a, b


x = [1, 2, 3, 4, 5]
y = [3, 5, 7, 9, 11]
# y = 2x + 1

a, b = least_squares(x, y)
print(f"y = {a:.4f} + {b:.4f}x")
