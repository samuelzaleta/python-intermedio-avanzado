myList =['banana','apple','cherry' ]
print(myList)
myList2 =[5,True,'apple','apple']
item =myList2[2]
print(item)
for i in myList:
    print(i)
if 'banana' in myList:
    print('Yes')
else: print('No')
#
length  = len(myList)
print(length)
myList.append('lemon')
print(myList)
myList.insert(1, 'blueberry')
print(myList)
item  =myList.pop()
print(item)
print(myList)
myList.remove('cherry')
myList2.clear()
print(myList2.clear())
print(myList.reverse())
print(myList.sort())
myList = [1,34,5,-5,7]
myList.sort()
print(myList)
myList2 = [9,7,5,3,2]
a = sorted("This is a test string from Andrew".split(), key=str.lower)
print(myList2)
print(a)
student_tuples = [('john', 'A', 15),('jane', 'B', 12),('dave', 'B', 10)]
b = sorted(student_tuples, key=lambda x: x[2])
print(b)
myList = [0] * 5
print(myList)
myList2 = [1,2,3,4,5]
newlist = myList + myList2
print(newlist)
myList = [1,2,3,4,5,6,7,8,9]
print(myList[1:5])
print(myList[::2])
myList = [1,2,3,4,5,6,7,8,9]
#copy1
newlist1 = myList.copy()
#copy2
newlist2 = list(myList)
#copy3
newlist3 = myList[:]
myList = [1,2,3,5,6,7]
b = [i*i for i in myList]
print(b)
myList = [1,2,3,4,5,6,6,7,8,9,1,2,4,5,6,7,8,9,12,3,4,5,6,6,6,67,8,9]
print(myList.count(6))
print(myList.index(67))