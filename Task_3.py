def main(a, b, x):
    res = 0
    for k in range(1, b+1):
        for c in range(1, a+1):
            res += 63 * k + 82 * ((c/83) - (c ** 3) / 94 - x ** 2) ** 5
    return res
