mySet ={1,2,3,4,1,1,1,2,2}
print(mySet) #{1, 2, 3, 4}
mySet = set([1,2,3,4,5,1,2,3,6])
print(mySet)
mySet = set('Hello')
print(mySet)
mySet = {'hello'}
print(mySet)
mySet = set(['hello','hello','Hello','Hello'])
print(mySet)
mySet = set()
mySet.add(1)
mySet.add(2)
mySet.add(4)
mySet.add(3)
print(mySet)
mySet.remove(3)
print(mySet)
#si no existe no manda error
mySet.discard(4)
print(mySet)
#pop elimina al primero
mySet.add(0)
a =mySet.pop()
print(mySet,a)
mySet.clear()
print(mySet)
mySet = set([1,2])
mySet.update([3,4,5,6,7])
print(mySet)
for i in mySet:
    print(i)
if 2 in mySet:
    print(True)
else: print(False)

odds ={1,3,5,7,9}
evens = {0,2,4,6,8}
primes ={2,3,5,7,11}

#unions
u= odds.union(evens)
#unions combine two set without duplication
print(u)
u = odds | evens
print(u)
#intersection
i = odds.intersection(primes)
print(i)
i = odds & primes
print(i)
setA ={1,2,3,4,5,6,7,8,9}
setB ={1,2,3,10,11,12}
diff = setA.difference(setB)
print(diff)
print((setA-setB))
diff = setB.difference(setA)
print(diff)
diff = setA.symmetric_difference(setB)
print(diff)
print(setB.symmetric_difference(setA))
print(setA.update(setB))
print(setA.intersection_update(setB))
#setA.issubset()
#setA.issuperset()
#setA.isdisjoint()
setA.add(20)
setA.remove(9)
