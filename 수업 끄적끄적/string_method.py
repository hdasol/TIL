a = 'apple'
print(a.find('p'))
print(a.find('x'))

print(a.index('p'))
# print(a.index('x'))

a = 'hello python!'
print(a.startswith('hello'))
print(a.endswith('hello'))

print('abc'.isalpha()) #True
print('ㄱㄴㄷ'.isalpha()) #True
print('Ab'.isupper()) #False
print('ab'.islower()) #True
print('Title Title!'.istitle()) #True
print('=============')
a = '    n'
b = '\n \t'
print(a.isspace()) #False
print(b.isspace()) #True
print('=============')
a = '파이썬'
b = 'python'
c = 'python 3.9.9'
print(a.isalpha()) #True
print(b.isalpha()) #True
print(c.isalpha()) #False
print('=============')

a = 'yaya!'
b = 'wooooowoo'
print(a.replace('y', 'h')) #haha!
print(b.replace('o', '_', 2)) #w__ooowoo
print('=============')

a = '   hello!  \n'
b = 'hihihihahahahihi'
c = 'monty python'

print(a.strip())
print(a.lstrip())
print(b.rstrip('hi'))

print(c.rstrip('python'))
print(c.rstrip(' python'))
print('=============')

a = 'a_b_c'
print(a.split('_')) #['a', 'b', 'c']

i = input('문자열 입력: ')
print(i.split(' '))









