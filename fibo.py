
def fibonacci(n):
    if n in (1,2):
        return 1
    return fibonacci(n - 2) + fibonacci(n - 1)


for i in range(1, 26):
    print(f'{i}: {fibonacci(i)}')

