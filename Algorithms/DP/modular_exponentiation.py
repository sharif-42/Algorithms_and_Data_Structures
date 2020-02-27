import timeit


def modular_exponentiation(x, n, m, d):
    """
    :param x: The number
    :param n: power
    :param m: modulo
    :param d: dictionary for lookup table or sometime called hash table
    :return:
    """
    if d.get(n):
        return d[n]
    else:
        if n % 2 == 0:
            y = modular_exponentiation(x, n // 2, m, d)
            d[n] = (y * y) % m
            print(n, d, y)
            return d[n]
        else:
            d[n] = (x % m) * (modular_exponentiation(x, n - 1, m, d) % m)
            print(n, d, d[n])
            return d[n]


if __name__ == '__main__':
    d = {0: 1}
    start_time = timeit.default_timer()
    mod = modular_exponentiation(2, 16, 3, d)
    print(mod)
    print("Execution Time: ", timeit.default_timer() - start_time)
