'''
파이썬06. 데이터 구조 및 활용 <데일리 홈워크>
'''

# 1. Built-in 함수와 메서드
# sorted()와 sort()의 차이점을 코드의 실행 결과를 활용하여 설명하시오.
# num.sort()는 오름차순으로 정렬해서 원래 변수에 저장해버린다!
# 하지만 sorted(num)은 원래 변수를 복사해서 새로운 변수를 오름차순해서 저장한다 

num = [7, 5, 1, 8, 3]
result = num.sort()
print(num, result) # [1, 3, 5, 7, 8] None
num = [7, 5, 1, 8, 3]
result = sorted(num)
print(num, result) # [7, 5, 1, 8, 3] [1, 3, 5, 7, 8]

# 2. extend()와 .append()
# .extend()와 .append()의 차이점을 코드의 실행 결과를 활용하여 설명하시오

cafe = ['americano', 'latte', 'chocolatte', 'cafucino']
print(cafe) # ['americano', 'latte', 'chocolatte', 'cafucino']
cafe.extend(['milk'])
print(cafe) # ['americano', 'latte', 'chocolatte', 'cafucino', 'milk']
cafe = ['americano', 'latte', 'chocolatte', 'cafucino']
cafe.extend('milk')
print(cafe) # ['americano', 'latte', 'chocolatte', 'cafucino', 'm', 'i', 'l', 'k']
# .extend()는 리스트에 리스트값과 문자열 값 둘다 추가할 수 있음
cafe = ['americano', 'latte', 'chocolatte', 'cafucino']
cafe.append('milk')
print(cafe) # ['americano', 'latte', 'chocolatte', 'cafucino', 'milk']

# 3. 복사가 잘 된건가?
# 아래의 코드를 실행 하였을 때, 변수 a와 b에 담긴 list의 요소가 같은지 혹은 다른지
# 여부를 판단하고 그 이유를 작성하시오.

a = [1, 2, 3, 4, 5]
b = a
a[2] = 5
print(a) #[1, 2, 5, 4, 5]
print(b) #[1, 2, 5, 4, 5]

# 이것은 얕은복사다. a 배열만 바꾸려고 했는데 b 배열도 바뀌었다. 각각의 변수가 같은 배열을
# 가르키고 있기 때문이다. 그래서 a의 변화가 b에도 영향을 줌...

a = [1, 2, 3, 4, 5]
b = a[:]
a[2] = 5
print(a) #[1, 2, 5, 4, 5]
print(b) #[1, 2, 3, 4, 5]

'''
파이썬 06. 데이터 구조 및 활용 <데일리 워크샵>
'''
# 1. 무엇이 중복일까
# 분자열을 전달 받아 해당 문자열에서 중복해서 나타난 문자들을 담은 list를 반환하는
# duplicated_letters 함수를 작성하시오.

a = '!'.join('apple')
b = a.split('!')
print(b) #['a', 'p', 'p', 'l', 'e']


def duplicated_letters(word):
    x = '!'.join(word)
    y = x.split('!')
    z = []

    for i in range(len(y)):
        if y[i] in y[i+1:len(y)]:
            z.append(y[i])
            
    return list(set(z))

print(duplicated_letters('apple'))


# 2.소대소대
# 문자열을 전달 받아 해당 문자열을 소문자와 대문자가 번갈아 나타나도록 변환하여
# 반환하는 low_and_up 함수를 작성하시오. 이때, 전달 받는 문자열은 알파벳으로만 구성된다.

def low_and_up(word):
    x = '!'.join(word)
    y = x.split('!')
    z = [] # ['b', 'A', 'n', 'A', 'n', 'A']
    
    for i in range(len(word)):
        if i % 2 == 1:
            z.append(word[i].upper())
        else:
            z.append(word[i])
    return ''.join(z) # z를 문자열로 변환한다 리스트 내부 문자를 다 합쳐

print(low_and_up('banana'))
print(low_and_up('apple'))

# 3.솔로 천국 만들기
# 정수 0부터 9까지 이루어진 list를 전달 받아, 연속적으로 나타나는 숫자는 하나만
# 남기고 제거한 list를 반환하는 lonely 함수를 작성하시오.
# 이때, 제거된 후 남은 수들이 담긴 list의 요소들은 기존의 순서를 유지해야 한다.

def lonely(num_list):

    lonely_list = []
    lonely_list.append(num_list[0])

    for i in range(1,len(num_list)):
        
        if num_list[i-1] != num_list[i]:
            lonely_list.append(num_list[i])
    return lonely_list

print(lonely([1, 1, 3, 3, 0, 1, 1]))
print(lonely([4, 4, 4, 3, 3]))








        
