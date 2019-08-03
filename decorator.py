

def ziomus(decorated):
    def wrapper(*args, **kwargs):
        return 'pfff'
    return wrapper

@ziomus
def test():
    return 'siemanko'


print(test())

