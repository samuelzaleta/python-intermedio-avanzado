import random

a  = random.random()
print(a)
a  = random.uniform(1,10)
print(a)
a = random.randint(1,10)
print(a)
a = random.randrange(1,10)
print(a)
#normal distribuition
a = random.normalvariate(0,1)
print(a)

mylist =list('ABDCEFH')
print(mylist)
a  =random.choice(mylist)
print(a)
a = random.sample(mylist,3)
print(a)
a = random.choices(mylist, k=3)
print(a)
#barajear
random.shuffle(mylist)
print(mylist)

random.seed(2)
print(random.random())
print(random.randint(1,10))
