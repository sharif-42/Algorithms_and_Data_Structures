def fibonacci(n):
    if n<=2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)


if __name__ == '__main__':
    fibo = fibonacci(8)
    print(fibo)
