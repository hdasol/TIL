'''
파이썬07. 객체 지향 프로그래밍

Faker는 개발시 활용할 수 있는 가상의 데이터를 생성해주는 파이썬 패키지이다.
워크샵에 등장하는 코드는 모두 Github(https://github.com/joke2k/faker) 문서의 예제이다.
지금까지 배운 파이썬 개념을 활용하여 해석하시오.
'''

# 1. $ pip install Faker 는 무엇을 위한 명령인지? 실행은 어디서 해야하는지? 작성
# 가짜 데이터를 쉽게 만들기 위한 패키지이다! cmd 또는 깃베쉬에서 설치할 수 있다


# 2. Faker는 다양한 메서드를 통해 임의의 결과값을 반환해준다.
# 임의의 영문 이름을 반환하는 아래 코드에서 라인별 의미를 주석을
# 참고하여 작성하시오.

from faker import Faker # 페이커 라이브러리를 가져온다
fake = Faker('ko_KR') # 객체 생성/ Faker()는 클래스 변수 / fake 인스턴스 변수
print(fake.name())
# name()메서드를 사용하면 간단하게 가짜 이름을 생성할 수 있음
'''
class Faker():
    def __init__(self, name):
        pass
'''


# 4. seeding the generator
# 컴퓨터 프로그래밍에서 임의의 값을 반환하는 경우(난수 생성 등) 시드라는
# 개념이 있다. 시드를 설정하게 되면 동일한 순서로 난수를 발생시킬 수 있어
# 일반적으로 디버깅을 위하여 활용된다.

import random

random.random()
print(random.random())
# random.random()은 [0,1) 사이의 실수로 난수를 구하며, 
# random.ranint(a,b) 는 [a,b] 사이의 정수로 난수를 구한다.

random.seed(7777)
print(random.random())

random.seed(8888)
print(random.random())
# 난수 발생을 위해서는 적절한 시드를 난수발생기에 주어야 한다.
# 만약 시드가 같다면 동일한 난수를 발생시키게 된다.
# 생성기는 시드 값 기반으로 난수 생성한다.
# 난수 생성하도록 (시드 값)으로 시작할 숫자가 필요.


# 아래의 코드를 실행 했을 때, #1과 #2에서 출력되는 결과를 각각 작성하고,
# seed()는 어떤 종류의 메서드인지 작성하시오.
# 값이 동일하게 출력된다!!! fake1은 '이진호' feke2는 '강은주'로 고정돼 출력

fake1 = Faker('ko_KR')
Faker.seed(87654321)

print(fake1.name()) #1 이진호

fake2 = Faker('ko_KR')
print(fake2.name()) #2 강은주


# 아래의 코드를 실행 했을 때, #1과 #2에서 출력되는 결과를 각각 작성하고,
# seed_instance()는 어떤 종류의 메서드인지 작성하시오.

fake1 = Faker('ko_KR')
fake1.seed_instance(87654321)

print(fake1.name()) #1 '이진호'로 고정

fake2 = Faker('ko_KR')
print(fake2.name()) #2 이름이 계속 변경