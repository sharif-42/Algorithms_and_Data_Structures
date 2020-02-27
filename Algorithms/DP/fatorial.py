import timeit


def factorial(n, d):
    if n == 1 or n == 0:
        return 1
    else:
        if d.get(n):
            return fact
        else:
            d[n] = n * factorial(n - 1, d)
            return d[n]


if __name__ == '__main__':
    start_time = timeit.default_timer()
    d = {
        0: 1,
        1: 1
    }
    fact = factorial(5, d)
    print(fact)
    end_time = timeit.default_timer()
    print("The Execution time for Factorial in DP :", timeit.default_timer() - start_time)
