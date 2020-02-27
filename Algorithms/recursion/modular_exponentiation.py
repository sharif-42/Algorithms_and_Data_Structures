import timeit


def modular_exponentiation(x, n, m):
    """
    :param x: The number
    :param n: power
    :param m: modulo
    :return:
    """
    if n == 0:
        return 1
    if n % 2:
        y = modular_exponentiation(x, n - 1, m)
        return (x % m) * (y % m)

    else:
        y = modular_exponentiation(x, n // 2, m)
        return (y * y) % m


if __name__ == '__main__':
    start_time = timeit.default_timer()
    mod = modular_exponentiation(2, 3, 3)
    print(mod)
    print("Execution Time: ", timeit.default_timer() - start_time)
