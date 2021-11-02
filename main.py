def fib(n):
    if n <=2:
        return 1
    print(n-1, n-2)
    return (n -1)  + (n -2)
def foo(n):
    if n <=1:
        return
    foo(n-1)
def dib(n):
    if n <= 1:
        return
    dib(n -1)
    dib(n -1)
def lib(n):
    if n <=1:
        return
    lib(n -2)
    lib(n -2)
print(fib(100000))
print(foo(50),'foo')
print(dib(5),'dib')
print(lib(2),'lib')