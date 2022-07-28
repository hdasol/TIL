'''
아래의 명세를 일고 python 클래스를 활용하여 사람(person)을 표현하시오.

1. 사람은 이름과 나이를 가진다. 
2. 사람을 인스턴스를 생성하는 방법은 2가지다.
   A. 생성자
     i. 이름과 나이를 인자로 받는다.
   B. details 클래스 메서드
     i. 이름과 태어난 년도를 인자로 받는다.
3. 인스턴스의 나이를 확인하는 메서드 check_age를 만든다.
   A. 미성년자의 기준을 미성년자 여부를 True, False로 반환한다. 미성년자는 19세를 기준으로 한다.
'''

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    
    @classmethod
    def details(cls, name, birth_years):
        cls.name = name
        cls.birth_years = birth_years

        return cls.name, cls.birth_years

    def check_age(self):
        if self.age > 19:
            return False
        else:
            return True

dasol = Person('다솔', 29)
print(dasol.check_age())
print(dasol.name)
print(dasol.age)
print(Person.details('다솔', 1994))