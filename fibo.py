
cache = {}


def fibonacci(n):
    if n in cache:
        return cache[n]

    if n in (1, 2):
        cache[n] = 1
        return 1

    cache[n] = fibonacci(n - 2) + fibonacci(n - 1)
    return cache[n]


for i in range(1, 100):
    print(f'{i}: {fibonacci(i)}')


def fib_decorator(decorated):
    cache = {}

    def wrapper(n):
        try:
            return cache[n]
        except KeyError:
            cache[n] = decorated(n)
            return cache[n]
    return wrapper


@fib_decorator
def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 2) + fibonacci(n - 1)


for i in range(1, 100):
    print(f'{i}: {fibonacci(i)}')