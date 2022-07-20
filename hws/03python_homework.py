'''
데일리 홈워크 03. 제어문과 함수
'''
# 1. bulit-in 함수
# python에서 기본으로 사용할 수 있는 built-in 함수를 최소 5가지 이상 작성하시오.
bulit_in = [print, len, chr, sum, sorted]
print(bulit_in)


# 2. 홀수만 담기
# range와 slicing을 활용하여 1부터 50까지의 숫자 중, 홀수로만 이루어진 리스트를 만드시오.
for i in range(1, 51):
    if i % 2 == 0:
        continue
    print(i, end=' ')
print()
print(list(range(1,51,2)))

# 3. 반복문으로 네모 출력
# 두 개의 정수 n과 m이 주어졌을 때, 가로의 길이가 n, 세로의 길이가 m인 직사각형 형태를
# 별(*) 문자를 이용해 출력하시오.
n = 5
m = 9

for i in range(m):
    for j in range(n):
        print("*", end="") # end에 ''를 지정하여 줄바꿈을 하지 않음
    print()

# 4. 조건 표현식
# 주어진 코드의 조건문을 조건 표현식으로 바꾸어 작성하시오.
temp = 36.5
if temp >= 37.5:
    print('입실 불가')
else:
    print('입실 가능')
print()

temp = 37.5
result = '입실 불가' if temp >= 37.5 else '입실 가능'
print(result)

# 5. 정중앙 문자
# 문자열을 전달 받아 해당 문자열의 정중앙 문자를 반환하는 get_middle_char 함수를
# 작성하시오. 단, 문자열의 길이가 짝수일 경우에는 정중앙 문자 2개를 반환한다.
# get_middle_char('ssafy') -> a
# get_middle_char('cofing') -> di

def get_middle_char(str):
    return str[(len(str)-1)//2:(len(str)//2)+1]

word = str(input('문자열을 입력: '))
print(get_middle_char(word))


'''
데일리 워크샵 03. 제어문
'''
# 1. 세로로 출력하기
# 자연수 number를 입력 받아, 1부터 number까지의 수를 세로로 한 줄씩 출력하시오.
num = int(input('자연수 입력: '))
for i in range(1,num+1):
    print(i)
print('02---------------------------')

# 2. 가로로 출력하기
# 자연수 number를 입력 받아, 1부터 number까지의 수를 가로로 한 칸씩 띄어 출력하시오.
num = int(input('자연수 입력: '))
for i in range(1,num+1):
    print(i, end=" ")
print()
print('03---------------------------')

# 3. 거꾸로 세로로 출력하기
# 자연수 number를 입력 받아, number부터 0까지의 수를 세로로 한 줄씩 출력하시오.
num = int(input('자연수 입력: '))
for i in range(num, -1, -1):
    print(i)
print('04---------------------------')

# 4. 거꾸로 출력해 보아요
# 자연수 number를 입력 받아, number부터 0까지의 수를 가로로 한칸씩 띄어 출력하시오.
num = int(input('자연수 입력: '))
for i in range(num, -1, -1):
    print(i, end=" ")
print()
print('05---------------------------')

# 5. N줄 덧셈
# 입력으로 자연수 number가 주어질 때, 1부터 주어진 자연수 number까지를 모두 더한
# 값을 출력하시오. 단, 주어지는 숫자는 10000을 넘지 않는다. 예를 들어, 주어진 숫자가
# 10일 경우 1+2+3+4+5+6+7+8+9+10 = 55 이므로, 출력해야할 값은 55이다.
num = int(input('자연수 입력: '))
result = 0
for i in range(1, num+1):
    result += i
print(result)
print('06---------------------------')

# 6. 삼각형 출력하기
# 자연수 number를 입력 받아, 아래와 같이 높이가 number인 삼각형을 출력하시오.
num = int(input('자연수 입력: '))
for i in range(1, num+1):
    print(' '*(num-i), end='')
    print('*'*i)
print('07---------------------------')

# 7. 중간값 찾기
# 중간값은 통례 집단의 수치를 크기 순으로 배열 했을 때 전체의 중앙에 위치하는 수치를
# 뜻한다. 리스트 numbers에 입력된 숫자에서 중간값을 출력하라.
numbers = [85, 72, 38, 80, 69, 65, 68, 96, 22, 49, 67, 51, 61, 63, 87, 66, 24, 80, 83, 71, 60, 64, 52, 90, 60, 49, 31, 23, 99, 94, 11, 25, 24]
A = sorted(numbers)
print(A[(len(A)-1)//2:len(A)//2+1])