from functools import reduce
add10  = lambda x: x+10
print(add10(5))
mult  = lambda x,y:  x*y
print(mult(7, 2))

point2D = [(1,2),(15, -1),(5, -1),(10,4),(10,7),(25,7)]
x  = sorted(point2D, key=lambda x: x[1])
print(x)
#map(func, list)
a = [1,2,3,4,5,6,7]
b = list(map(lambda x:x*2,a))
print(b)
c = [x * 2 for x in a]
print(c)

#filter(funcion, sq)
b = list(filter(lambda x: x%2==0,a))
print(b)
c = [x for x in a if x%2 ==0]
print(c)

#reduce (func,seq)
a = [1,2,3,4]

producyt_a = reduce(lambda x,y: x*y,a)
print(producyt_a)
