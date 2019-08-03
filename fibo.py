
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

