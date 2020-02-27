import timeit


def power(x, n, d):
    print(x, n, d)
    if n == 0:
        return 1
    if n == 1:
        return x
    if d.get(n):
        return d[n]
    else:
        if n % 2:
            d[n] = x * power(x, n - 1, d)
            return d[n]
        else:
            y = power(x, n // 2, d)
            d[n] = y * y
            return d[n]


if __name__ == '__main__':
    x, n = 10, 10
    d = {
        0: 1,
        1: x,
    }
    start_time = timeit.default_timer()
    print(power(x, n, d))
    print("Execution Time: ", timeit.default_timer() - start_time)
