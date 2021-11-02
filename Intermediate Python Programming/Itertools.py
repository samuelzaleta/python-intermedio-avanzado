from itertools import product
from itertools import permutations
from itertools import combinations , combinations_with_replacement
from itertools import accumulate
import operator
from itertools import groupby
from itertools import count, cycle, repeat
a =[1,2]
b =[3,4]
prod  = product(a,b)
#combine [(1, 3), (1, 4), (2, 3), (2, 4)]
print(list(prod))
a =[1,2]
b =[3]
prod  = product(a,b, repeat = 2)
#[(1, 3, 1, 3), (1, 3, 2, 3), (2, 3, 1, 3), (2, 3, 2, 3)]  ->2[1,3] [1,3,2,3] ->2[2,3]
print(list(prod))
dado1 = [1,2,3,4,5,6]
dado2 = [1,2,3,4,5,6]
prod = list(product(dado2,dado1))
print(prod)
p = list(filter(lambda x:x[0] + x[1] == 7,prod))
print(p)

a = [1,2,3]
perm = list(permutations(a))
#permutaciones 1,2,3 ->[(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
#En matemáticas, una permutación es la variación del orden o posición de los elementos de un conjunto ordenado o una tupla
print(perm)
print(len(perm))
print(list(permutations(a, 2)),'\n')
a = [1,2,3,4]

comb = list(combinations(a,2))
print(comb)
b =[1,2,3,4,5,6,1,2,3,4,5,6]
comb =  list(combinations(b,3))
print(comb)
comb = list(combinations(a,2))
print(comb)
comb_wr = list(combinations_with_replacement(a,2))
print(comb_wr)


acc = accumulate(a)
print(a)
print(list(acc))
acc = accumulate(a, func=operator.mul)
print(list(acc))
a =[1,2,4,5,4,3,2, 6,7,2,9,1,1]
acc = accumulate(a, func=max)
print(a)
print(list(acc))


def smaller_than_3(x):
    return x < 3
a =[1,2,3,4]
gruop_obj = groupby(a, key=smaller_than_3)
for k,v in gruop_obj:
    print(k,list(v))
gruop_obj = groupby(a, key=lambda x: x<3)
persons = [{'name':'Tim', 'age':25},{'name':'Dan', 'age':25},
           {'name':'Lisa', 'age':27},{'name':'Claire', 'age':28}]
gruop_obj = groupby(persons, key=lambda x: x['age'])
for k,v in gruop_obj:
    print(k, list(v))


#count
for i in count(10):
    print(i)
    if i ==25:
        break
#cycle
a = [1,2,3]
c = 0
for i in cycle(a):
    print(i)
    if c >20:
        break
    c += i
#repeat
#repeat(x, stop)
for i in repeat(1, 4):
    print(i)