
def name(decorated):
    def wrapper(*args):
        name = input('Podaj swoje imię: ')
        return f'{decorated()} {name}'
    return wrapper


@name
def hello_world():
    return 'Hello'

print(hello_world())