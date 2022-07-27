'''
파이썬07. 객체 지향 프로그래밍_데일리 홈워크
'''

# 1. Type Class
# 파이썬은 객체 지향 프로그래밍 언어다. 파이썬에서 기본적으로 정의되어 있는
# 클래스를 최소 5가지 이상 작성하시오.

# 답: <class 'int'> <class 'list'> <class 'tuple'> <class 'str'> <class 'dict'>
print(type('3')) # <class 'str'>
print(type(3)) # <class 'int'>
print(type([1, 2, 3])) # <class 'list'>
print(type((1, 2, 3))) # <class 'tuple'>
print(type({1:'학생', 2:'선생님', 3:'교장'})) # <class 'dict'>

print('====================================================')

# 2. Magic Method
# 아래 제시된 매직 메서드들이 각각 어떠한 역할을 하는지 간단하게 작성하시오.
# __init__, __del__, __str__, __repr__

# __init__
# 생성자를 호출하여 클래스의 새 인스턴스를 인스턴스화하려고 할 때 생성
# 클래스의 인스턴스를 생성할 때 자동으로 호출되며, 일반적으로 인스턴스 생성과
# 함께 인스턴스 변수를 선언하기 위해 사용된다.

# __del__
# 객체가 삭제될 때 호출되는 메소드

# __str__
# 객체를 사람이 이해할 수 있는 문자열로 만들어 준다.
# 이 메소드를 오버라이딩 해주지 않으면 해당 객체의 메모리상 위치를 반환한다.

# __repr__
# 'representation'의 약자. repr 함수는 어떤 객체의 '출력될 수 있는 표현'을 
#  문자열의 형태로 반환하다. 

# __str__, __repr__ 의 공통점
# 객체가 어떤 데이터 타입인지든지간에 객체의 문자열 표현을 반환한다. 
# __str__ 평문화, __repr__ 객체를 표하는데 중점!
# __str__ 메소드를 정의하지 않았다면 __repr__ 메소드가 대신 쓰인다!

print('====================================================')

# 3. instance method
# .sort()와 같이 문자열, 리스트, 딕셔너리 등을 조작할 때 사용했던 것들은
# 클래스에 정의된 메서드들이었다. 이처럼 문자열, 리스트, 딕셔너리 등을
# 조작하는 메서드를 최소 3가지 이상 그 역할과 함께 작성하시오.

# .split() 공백 문자를 기준으로 문자열을 분리하여 list로 저장
# .append(n) 리스트에 값 n을 추가한다
# .pop() 리스트의 끝을 삭제하고 반환한다

print('====================================================')

# 4. 오류의 종류
# 아래에 제시된 오류들이 각각 어떠한 경우에 발생하는지 간단하게 작성하시오.
# ZeroDivisionError, NameError, TypeError, IndexError, KeyError
# ModuleNotFoundError, ImportError
'''
실행 중에 감지되는 에러들을 예외(exception)라고 부름
ZeroDivisionError : 0으로 나누고자 할 때 발생
NameError : namespace상에 이름이 없는 경우

TypeError : 타입이 불일치 할때 생기는 에러로 가령 int와 str의 계산이랄지
argument 누락시, argument 개수 초과, argument 타입 불일치에 타입에러가 뜸.

IndexError : 인덱스가 존재하지 않거나 범위를 벗어나는 경우
KeyError : 해당 키가 존재하지 않는 경우

ModuleNotFoundError : 정의되지 않는 모듈을 불러로는 경우
ImportError : 모듈은 있으나 존재하지 않는 클래스/함수를 가져오는 경우
'''



