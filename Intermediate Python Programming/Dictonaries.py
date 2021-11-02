myDict ={"name": "Max", "age":28, "city":"New York"}
print(myDict)
myDict2 = dict(name= 'Mary', age =37, city= 'Boston')
print(myDict2)
value = myDict['age']
myDict['email'] ='zaletadev@gmail.com'

del myDict['name']
print(myDict)
myDict['name'] ='Samue Zaleta Magaña'
myDict.pop("age")
print(myDict)
myDict.popitem()
print(myDict)
myDict['age'] =22
myDict['city'] ='Tampico'
myDict['name'] ='Samue Zaleta Magaña'
print(myDict)

if 'name' in myDict:
    print(True)
else: print(False)

if 'Tampico' in myDict.values():
    print(True)
else: print(False)

for key in myDict:
    print(key)

for key in myDict.keys():
    print(key)

for value in myDict.values():
    print(value)

for k,v in myDict.items():
    print(k,v)
newdict =myDict.copy()
#dict(myDict)

newdict['email'] ='samuel.zaleta.cbtis103@gmail.com'
print(myDict)
print(newdict)

my_dict  ={'name':'max','age':28,'city':'boston'}
my_dict2 = dict(name = 'Mary', age= 27, email = 'mary@yzc.com')
my_dict.update(my_dict2)
print(my_dict)
mytuple =(8,7)
#los tuples si pueden ser llaves, pero no las lista
mydict = {mytuple:17}
print(mydict)