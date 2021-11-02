#error an exception
x = 5
'''
if x < 0:
    raise Exception('x should be positive')

'''
assert(x >=0), 'X is no positive'
try:
    a = 5/0
except Exception as e:
    print(e)
try:
    a = 5/0
    b = a + 10
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
else:
    print('everything is fine')
finally:
    print('clean up...')

class ValueTooHighError(Exception):
    print('Valye is high')

class ValueTooSmallError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value

def test_value(x):
    if x >100:
        raise ValueTooHighError
    if x < 5:
        raise ValueTooSmallError('Value is small', x)
try:
    test_value(2)
except ValueTooHighError as e:
    print(e)
except ValueTooSmallError as e:
    print(e.message, e.value)