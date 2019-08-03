

def ziomus(decorated):
    def wrapper(*args, **kwargs):
        print('ble')
        return decorated()
    return wrapper

@ziomus
def test():
    return 'siemanko'


print(test())

