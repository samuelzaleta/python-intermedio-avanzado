import sys
from functools import reduce
def mygenerator():
    yield 1
    yield 2
    yield 3

g = mygenerator()
value = next(g)
print(value)
value = next(g)
print(value)
print(g)
for i in g:
    print(1)

def mygenerator():
    yield 1
    yield 2
    yield 3
g  = mygenerator()
print(sum(g))
#print(sorted) [1,2,3]

def countdown(num):
    print('Starting')
    while num > 0:
        yield num
        num -=1
cd = countdown(4)
print(cd)
value = next(cd)
print(value)
print(next(cd))

def firstn(n):
    nums = []
    num = 0
    while num < n:
        nums.append(num)
        num += 1
    return nums

def firstn_generator(n):
    num = 0
    while num < n:
        yield num
        num +=1
print(sys.getsizeof(firstn(1000000)))
print(sys.getsizeof(firstn_generator(1000000)))

#las veces
def fibonacciN(limit):
    #0,1,1,2,3,5
    a,b = 0,1
    while limit > 0:
        yield a
        #0,1,1,2,3...
        a,b = b, a+b
        limit -=1
fib = map(lambda x: x, fibonacciN(30))
print(list(fib))
fib  =  reduce(lambda x,y :x+y,fibonacciN(30))
print(fib)
def fibonacci(limit):
    a,b = 0,1
    while a < limit:
        yield a
        a,b =b, a+b
fib = fibonacci(30)
for i in fib:
    print(i)

mygenerator2 =(i for i in range(10000) if i%2 ==0)
print(mygenerator2)
'''
for i in mygenerator2:
    print(i)
'''
mylis = [i for i in range(10000) if i%2 ==0]
print(sys.getsizeof(mylis))
print(sys.getsizeof(list(mylis)))