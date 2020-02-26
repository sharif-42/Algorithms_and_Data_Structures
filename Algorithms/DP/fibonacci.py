import timeit


def fibonacci(n, d):
    # print(*d.values())
    if n == 1 or n == 0:
        return n
    else:
        if d.get(n):
            return d[n]
        else:
            d[n] = (fibonacci(n - 1, d) + fibonacci(n - 2, d))
            return d[n]


def fibo(n):
    if n == 1 or n == 0:
        return n
    else:
        return fibo(n - 1) + fibo(n - 2)


if __name__ == '__main__':
    d = {
        1: 1,
        2: 1,
    }
    start_time = timeit.default_timer()
    print(fibonacci(900, d))
    print("The Execution time for fibonacci in DP :", timeit.default_timer() - start_time)

    start_time = timeit.default_timer()
    print(fibo(40))
    print("The Execution time for fibonacci in recursion :", timeit.default_timer() - start_time)
