my_strin = "Hello World"
print(my_strin)
print("I\'m")
my_strin = """
HELLO \
WORLD
"""
print(my_strin)
my_string = 'hello word'
char = my_string[-1]
print(char)
subtring =  my_string[:5]
print(subtring)
subtring = my_string[::-1]
print(subtring)
greeting  = 'hello'
name ='Samuel'
sentence  = greeting + ' ' + name
print(sentence)
for x in greeting:
    print(x)
if 'e' in greeting:
    print(True)
else: print(False)
my_string = '   hello    '
my_string = my_string.strip()
print(my_string)
print(my_string.lower())
print(my_string.upper())
print(my_string.startswith('H'))
print(my_string.endswith('o'))
print(my_string.find('lo'))
print(my_string.count('l'))
print(my_string.replace('l','d'))
my_string = 'how are you doing'
my_string = my_string.split(' ')
print(my_string)
new_string = ' '.join(my_string)
print(new_string)
my_list = ['a'] * 6
print(my_list)
my_string = ''
for i in my_list:
    my_string += i
print(my_string)
my_list = ['a'] * 6
my_string =  ''.join(my_string)
print(my_string)
#print(my_strin.translate(my_strin.maketrans('l','G')))