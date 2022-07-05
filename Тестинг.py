def main(x, z):
    value = 0
    n = len(x)
    for i in range(1, len(x) + 1):
        value += 88 * (41 * x[n - i] ** 2 + 14 * z[i - 1])
    return 12 * value


print(main([-0.54, -0.99, 0.59, 0.23, 0.36, -0.53, -0.94], [0.16, 0.73, -0.81, -0.52, -0.85, -0.5, 0.18]))
