import sys
myTuple  = ('Max',4,'boston')
myTupleE =1,3,5
print(myTuple)
print(myTupleE)
print(type(myTupleE))
myTuple =  tuple(['Max',8,'Boston'])
print(myTuple)
item  = myTuple[0]
print(item)
for i in myTuple:
    print(i)
if 'Max' in myTuple:
    print(True)
else: print(False)
myTuple2 =1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,6,6,6,6,6,6,6,7,8,9,99
print(myTuple2.count(6))
print(myTuple2.index(99))
my_list = list(myTuple)
my_tuple2 =  tuple(my_list)
a =(1,2,3,4,5,6,7,8,9)
b = a[:5]
print(b)
my_tuple ='Max',28,'Boston'
name, age, city  =  my_tuple
my_tuple3 = (1,2,3,4,5,6)
i1,i2,*i3,i4 = my_tuple3
print(i3,i4)
my_tuple4 = (1,2,3,4,5,6,7,8,9)
my_list = [1,2,3,4,5,6,7,8,9]
print(sys.getsizeof(my_list),"Bytes")
print(sys.getsizeof(my_tuple4),"Bytes")
