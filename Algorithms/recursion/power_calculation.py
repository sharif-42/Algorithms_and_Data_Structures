import timeit


def power(x, n):
    if n == 0:
        return 1
    if n == 1:
        return x

    else:
        if n % 2:
            return x * power(x, n - 1)

        else:
            y = power(x, n // 2)
            return y * y


if __name__ == '__main__':
    x, n = 10, 10
    start_time = timeit.default_timer()
    print(power(2, 32))
    print("Execution Time: ", timeit.default_timer() - start_time)
