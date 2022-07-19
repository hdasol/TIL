#1 python에서 사용할 수 없는 식별자(예약어)
import keyword
print(keyword.kwlist)

#2 실수 비교
num1 = 0.1 *3
num2 = 0.3
print(num1, num2)
import math
print(math.isclose(num1, num2))

#3
print('\\n', '\\t', '\\')

#4
name = '철수'
print('안녕,'+name+'야')

#5 오류가 발생하는 코드 int('3.5')

#6
print("*" * 5)
print("*" * 5)
print("*" * 5)
print("*" * 5)
print("*" * 5)
print("*" * 5)
print("*" * 5)
print("*" * 5)
print("*" * 5)

#7
print('"파일은 c:\Windows\내문서\python에 저장이 되었습니다."\n나는 생각했다.\t\'cd를 써서 git bash로 들어가 봐야지\'')
print()
#8 근의 공식
def queadratic_formula(a,b,c):
    D = (b**2) - (4*a*c)
    
    if D>0:
        x1 = (-b + D**0.5) / (2*a)
        x2 = (-b - D**0.5) / (2*a)
        print(a,"x^2 + ",b,"x + ",c,"의 해는")
        print("{} 또는 {} 입니다.".format(x1,x2))
    elif D==0:
        x = -b / 2*a
        print("중근입니다. 해는 {}입니다.". format(x))
    else:
        print("허근입니다.")

 
print("2차방정식의 두 해를 구하는 근의 공식(quadratic fomula) 입니다.")
print("2차방정식은 ax^2+bx+c의 형태 입니다. 단 a는 0이 아닙니다.")
a=int(input("a를 입력해주세요."))
b=int(input("b를 입력해주세요."))
c=int(input("c를 입력해주세요."))
queadratic_formula(a,b,c)

print('---------------------------------------------')

'''
daily workshop
python 01. 기초문법과 데이터의 입출력
'''
# 1. 문자 print
print("lt's SSAFY 8")

# 2. 숫자 print
n = int(458345)
m = int(623576)
print(n+m) 

# 3. 변수를 사용해서 데이터 출력하기
greeting = 'Hello'
month = 'July'
print(greeting + month)

# 4. 문자형의 입력과 출력
hello = input()
print(hello)
