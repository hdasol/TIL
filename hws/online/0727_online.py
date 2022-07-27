'''
문제
개의 속성과 행위를 정의하는 Doggy 클래스를 만들어라.

구성요소
1. 초기화 메서드는 인자로 개의 이름과 견종을 받아서 인스턴스 변수에 할당한다.
2. bark() 메서드를 호출하면 개는 짖을 수 있다.
3. 클래스 변수는 태어난 개의 숫자와 현재 있는 개의 숫자를 기록하는 변수로 구성한다.
    개가 태어나면 num_of_dogs와 birth_of_dogs의 값이 각 1씩 증가한다.
    개가 죽으면 num_of_dogs의 값이 1감소한다.
4. get_status() 메서드를 호출하면 num_of_dogs와 birth_of_dogs의 수를 출력할 수 있다.
'''

class Doggy:
    num_of_dogs = 0
    birth_of_dogs = 0

    # 인스턴스 변수 설정
    def __init__(self, dog_name, dog_species):
        self.dog_name = dog_name
        self.dog_species = dog_species
        Doggy.birth_of_dogs += 1
        Doggy.num_of_dogs += 1
    
    def __del__(self):
        Doggy.num_of_dogs -= 1
    
    def bark(self, dog_name):
        return (f'{dog_name}는 멍멍')
        
dog1 = Doggy('뽀삐', '시츄')
dog2 = Doggy('초코', '푸들')

print(f'강아지 이름은 {dog1.dog_name}, 견종은 {dog1.dog_species}')
print(f'강아지 이름은 {dog2.dog_name}, 견종은 {dog2.dog_species}')
print(dog1.bark(dog1.dog_name))
print(dog1.bark(dog2.dog_name))
print(f'태어난 강아지는 {Doggy.birth_of_dogs} 마리, 강아지는 총 {Doggy.num_of_dogs} 마리')
print('뽀삐가 죽었다')
del(dog1) # 뽀삐가 죽었다
print(f'태어난 강아지는 {Doggy.birth_of_dogs} 마리, 강아지는 총 {Doggy.num_of_dogs} 마리')