from operator import index


a = [1, 2, 3, 4]
print(str(a)) #[1, 2, 3, 4]
print(tuple(a)) #(1, 2, 3, 4)
print(set(a)) #{1, 2, 3, 4}
# range(a)
# dict(a)

t = (1, 2, 3, 4)
print(str(t), type(str(t)))  #(1, 2, 3, 4) <class 'str'>
print(list(t), type(list(t))) #[1, 2, 3, 4] <class 'list'>
print(set(t), type(set(t))) #{1, 2, 3, 4} <class 'set'>

d = {'name':'ssafy', 'year':2022}
print(str(d)) #{'name': 'ssafy', 'year': 2022}
print(list(d)) #['name', 'year']
print(tuple(d)) #('name', 'year')
print(set(d)) #{'year', 'name'}

x = 3
print(x is None) #False

### 복합연산자!
cnt = 0
while cnt < 5:
    print(cnt)
    cnt = cnt + 1

print(-3 in range(3)) #False

print([0]*8) #[0, 0, 0, 0, 0, 0, 0, 0]
print((1, 2)*3) #(1, 2, 1, 2, 1, 2)
# print(range(1)*3)

print('abc'[0]) # a

str_a = 'apple'
# print(str_a[99]) #IndexError: string index out of range
print(-3**6) # -729
print((-3)**6) # 729

# 입력 받은 수를 세제곱으로 반환하는 함수!
def cute(x):
    return x ** 3
print(cute(2)) #8

def my_max(num):
    return max(num)

x = [1, 2, 3, 5, 6]
print(my_max(x)) #6

# 거꾸로 해도 우영우

wu_list = ['기러기', '우영우', '토마토', '박상권', '역삼역', '인도인', '황다솔', '010']


def wu_code(a):
    reverse = []
    for wu in wu_list:
        
        if wu == wu[::-1]:
            reverse.append(wu)
    return reverse

print(wu_code(wu_list))    


name = ['박상권', '우영우', '황다솔']
job = ['세무사', '변호사', '학생']

print(name.index('박상권'))

for i in name:
    for j in job:
        if name.index(i) == job.index(j):
            print(f'안녕하세요 {i} {j}입니다')



def rectangle(a,b):

    return a*b,2*(a+b)

print(rectangle(30,20))

'''
def my_list_max(a,b):
    if sum(a) > sum(b):
        return a
    elif sum(a) > sum(b):
        return a,b
    else:
        return b

print(my_list_max([10, 3], [5, 9]))
'''
def my_list_max(a,b):
    max_a, max_b = 0, 0
    for i in a:
        max_a = max_a + i
    for j in b:
        max_b = max_b + j
    
    if max_a > max_b:
        return a
    elif max_b > max_a:
        return b
    else:
        return a,b

print(my_list_max([10, 3], [5, 9]))


r = int(input('반지름 입력: '))
h = int(input('높이 입력: '))

def cylinder(r,h):
    return 3.14*r**2*h

print(cylinder(r,h))


name = input('이름 입력: ')

def greeting(name):
    if name == '':
        return '익명, 안녕?'
    else:
        return name+', 안녕?'

print(greeting(name))


def my_max(*x):  #가변인자 리스트
    max_x = 0
    for i in x:
        if i > max_x:
            max_x = i
    return max_x

print(my_max(10, 20, 30, 50))



sore_date = {'파이썬':87, '자바':55, 'c언어':60}
score =[sore_date['파이썬'], sore_date['자바'], sore_date['c언어']]
print(score) #[87, 55, 60]


def max_score(score):

    max_score = 0
    
    for i in score:
        if i > max_score:
            max_score = i
    return max_score

print(max_score(score))

restaurant = {'menus':['라면', '김밥', '돈까스']}
print(len(restaurant['menus']))

max1 = [9, 9, 11, 11, 8, 7]
min2 = [3, 0, -3, -1, -3, 5]

temp_dict = {'maximum':max1, 'minimum':min2}
print(temp_dict)

a = [1, 2, 3, 4, 5, 6]
a.reverse()
print(a)
# b = a.reverse()
# print(b)가 출력 안 된다! None으로 뜸

b = [1, 2, 3, 4, 5, 6]
c = b[::-1]
print(c)