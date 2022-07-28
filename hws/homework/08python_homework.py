'''
파이썬08. 객체 지향 프로그래밍_데일리 홈워크
'''
# 1. circle 인스턴스 만들기
# 아래와 같은 Circle 클래스가 있을 때, 반지름이 3이고 x,y좌표가 (2,4)인
# Circle 인스턴스를 만들어 넓이와 둘레를 출력하시오.

class Circle:
    pi = 3.14

    def __init__(self,r,x,y):
        self.r = r
        self.x = x
        self.y = y

    def area(self): # 원의 넓이
        return Circle.pi*self.r*self.r

    def circumference(self): #원의 지름
        return 2*Circle.pi*self.r

    def center(self): # 원의 중점
        return(self.x,self.y)


circle01 = Circle(3,2,4)
print(circle01.area())
print(circle01.circumference())
print(circle01.center())


# 2. Dog과 Bird Animal이다
# 다음과 같이 Animal 클래스가 주어질 때, 해당 클래스를 상속 받아 아래의 보기와
# 동작하는 Dog 클래스와 Bird 클래스를 작성하시오.

class Animal:
    def __init__(self,name):
        self.name = name

    def walk(self):
        print(f'{self.name}! 걷는다!')

    def eat(self):
        print(f'{self.name}! 먹는다!')

class Dog(Animal):
    def __init__(self,name):
        self.name = name
    
    def run(self):
        print(f'{self.name}! 달린다!')

    def bark(self):
        print(f'{self.name}! 짖는다!')

class Bird(Animal):
    def __init__(self,name):
        self.name = name
    
    def fly(self):
        print(f'{self.name}! 푸드덕!')

dog = Dog('꼽이')
dog.run()
dog.bark()

bird = Bird('구구')
bird.walk()
bird.eat()
bird.fly()

# 3. Module Import

# fibo.py

def fibo_recursion(n):
    if n < 2:
        return n
    else:
        return fibo_recursion(n-1) + fibo_recursion(n-2)

# 위와 같은 코드가 같은 폴더 안의 fibo.py 파일에 작성되어 있을 때, 아래와 같은
# 형태로 함수를 실행 할 수 있도록 하는 import 문을 빈칸 (a), (b), (c)를 채워
# 넣어 완성하시오.

from fibo import fibo_recursion as recursion 

print(recursion(4))


'''
파이썬08. 객체 지향 프로그래밍_데일리 워크샵
'''

# 1. 도형 만들기
# 아래의 명세를 읽고 python 클래스를 활용하여 점(point)과 사각형(Rectangle)을 표현하시오.

# Point 클래스에 대한 명세는 다음과 같다.

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
p1 = Point(4,3)

class Rectangle:
    def __init__(self,p1,p2):
        self.p1 = p1
        self.p2 = p2
        
    
    def get_area(self):
        return abs(self.p2.x - self.p1.x)*abs(self.p1.y - self.p2.y)
    
    def get_perimeter(self):
        return ((abs(self.p2.x - self.p1.x)+abs(self.p1.y - self.p2.y))*2)
    
    def is_square(self):
        if abs(self.p2.x - self.p1.x) == abs(self.p1.y - self.p2.y):
            return True
        else:
            return False




p1 = Point(1,3)
p2 = Point(3,1)
r1 = Rectangle(p1,p2)
print(r1.get_area())
print(r1.get_perimeter())
print(r1.is_square())

p3 = Point(3,7)
p4 = Point(6,4)
r2 = Rectangle(p3,p4)

print(r2.get_area())
print(r2.get_perimeter())
print(r2.is_square())

