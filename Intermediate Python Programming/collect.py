from collections import Counter
from collections import namedtuple
from collections import OrderedDict
from collections import defaultdict
from collections import deque
a = 'aaaaaaabbbcccccccc'
my_counter  = Counter(a)
print(my_counter)
print(my_counter.items())
print(my_counter.keys())
print(my_counter.values())
print(list(zip(my_counter.keys(), my_counter.values())))
print(my_counter.most_common())
print(my_counter.most_common(2))
print(my_counter.most_common()[0])
print(my_counter.most_common()[0][0])
print(my_counter.elements())
print(list(my_counter.elements()))
Point = namedtuple('Point', 'x,y')
pt = Point(1,-4)
print(pt)
print(pt.x, pt.y)
ordere_dict = OrderedDict()
ordere_dict['c'] =3
ordere_dict['d'] =4
ordere_dict['a'] =1
ordere_dict['b'] =2
ordere_dict['f'] =5
print(ordere_dict)
d = defaultdict(float)
d['a'] = 1
d['b'] = 2
print(d['c'])
d = deque()
d.append(1)
d.append(2)
print(d)
d.appendleft(3)
print(d)
d.pop()
print(d)
d.popleft()
print(d)
d.clear()
print(d)
d.extend([4,5,6])
d.extendleft([1,2,3]) #deque([3, 2, 1, 4, 5, 6])
print(d)
d.rotate(1)
print(d)
d.rotate(-1)
print(d)
d.rotate(-1)
print(d)