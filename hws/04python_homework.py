'''
phthon 04. 함수 심화 데일리 홈워크
'''

# 1. 위치 인자와 키워드 인자
# (4)번 오류다. 처음에 인자를 정의해주면 뒤에도 정의해줘야한다. 컴퓨터는 일관적인 것을 좋아한다.

# 2. 가변 인자 리스트

grade = [77, 83, 95, 80, 70]


def my_avg(grade):
    return sum(grade)/len(grade)

print(my_avg(grade))

# 3. 반화값
# 10이 저장된다. my_func 함수가 안에 있는 인자를 더해 반환하기 때문.

def my_func(a, b):
    c = a + b
    print(c)

result = my_func(3, 7)

# 4. 이름 공간
# python에서 변수를 찾을 때 접근하는 이름 공간을 순서대로 작성하시오.
print('local scope, enclosed scope, global scope, built-in scope')

# 5. 매개변수와 인자, 그리고 반환 : 답은 (1)!!! 
# (1) 함수는 두 개 이상의 객체를 반환할 수 있다. but return을 두 번 쓰는 것은 안돼!
# (2) 함수는 return을 작성하지 않으면 None 값을 반환한다.
# (3) Argument? 함수를 호출할 때, 넣어주는 값 / parameter? 함수를 선언할 때 설정한 값.
# (4) *는 스퀸스 언패킹 연산자, 주로 튜플이나 리스트를 언패킹! 함수내에서 tuple로 처리
num = (1, 2, 3, 4, 5)
a, b, *rest = num
print(rest, type(rest))

def func(*args):
    print(args)
    print(type(args))
func(1, 2, 3, 'a', 'b')

# 6. 재귀함수
# 재귀 함수를 사용했을 때 얻을 수 있는 장점과 단점을 반복문과 비교하여 작성하시오.
# 재귀 함수는 자기 자신을 호출하는 함수
# 재귀 호출은 변수 사용을 줄여줄 수 있음, 재귀 호출은 입력 값이 커질 수록 연산 속도가 오래 걸림.

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(4))

def fac(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result
print(fac(4))




'''
phthon 04. 함수 심화 데일리 워크샵!!!!
'''
# 1. 간단한 N의 약수 1, 2, 3, 5, 7

N = int(input('정수를 입력: '))

def divisior(N):
    divisior_list = []

    for i in range(1, N+1):
        if N % i == 0:
            divisior_list.append(i)

    return divisior_list

print(divisior(N))

# 2. List의 합 구하기

A = [1, 2, 3, 4, 5]


def list_sum(A):
    result = 0
    for i in range(len(A)):
        result += A[i]
    return result

print(list_sum(A))

# 3. Dictionary로 이루어진 List의 합 구하기

B = [{'name': 'kim', 'age': 12}, {'name': 'lee', 'age': 4}]

def dict_list_sum(B):
    K = 0
    for i in range(len(B)):
        K += B[i]['age']
    return K
print(dict_list_sum(B))

# 4. 2차원 List의 전체 합 구하기

C = [[1], [2, 3], [4, 5, 6], [7, 8, 9, 10]]

def all_list_sum(C):
    list_sum = 0
    for i in range(len(C)):
        for j in range(i+1):
            list_sum += C[i][j]
    return list_sum
print(all_list_sum(C))

# 5. 숫자의 의미
print(chr(122))
print(chr(83))

list_word = [83, 115, 65, 102, 89]

def get_secret_word(list_word):
    bin = ''
    for i in range(len(list_word)):
        bin += chr(list_word[i])
    return bin
        
print(get_secret_word(list_word))

# 6. 내 이름은 몇일까?

word = 'happy'







