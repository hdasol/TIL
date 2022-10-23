'''
온라인수업_0725(월)
파이썬:데이터 구조 및 활용
'''

word = 'ssafy'
print(word)
print(id(word)) # 메모리 주소 확인 2117298542832
word = 'test'
print(word) #원래 word는 'ssafy' 였는데 'test'로 덮어씀
print(id(word)) # 메모리 주소 확인 2117298470960


# 문자열 조회/탐색 및 검증 메서드

s = 'happy'

print(s.find('p')) # x의 첫 번째 위치를 반환. 없으면, -1을 반환 -> 프로그램 진행
print(s.index('p')) # x의 첫 번째 위치를 반환. 없으면, 오류 발생 -> 프로그램 스탑!

print('apple'.find('p')) # 1
print('apple'.find('x')) # -1 -> x가 없다!

# print('apple'.index('x')) -> 오류 난다!

print('abc'.isalpha()) # True
print('ㄱㄴㄷ'.isalpha()) # True

print('Ab'.isupper()) # False

print('a,b,c'.split(',')) #['a', 'b', 'c']
print('a b c'.split()) #['a', 'b', 'c']
print('서울시 강남구 역삼동'.split()[0]) #서울시

msg = 'hI! Everyone, I\'m ssafy'
print(msg) # hI! Everyone, I'm ssafy
print(msg.capitalize()) # Hi! everyone, i'm ssafy
print(msg.title()) # Hi! Everyone, I'M Ssafy
print(msg.upper()) # HI! EVERYONE, I'M SSAFY
print(msg.lower()) # hi! everyone, i'm ssafy
print(msg.swapcase()) # Hi! eVERYONE, i'M SSAFY

cafe = ['starbucks', 'tomntoms', 'hollys']
print(cafe, id(cafe)) # ['starbucks', 'tomntoms', 'hollys'] 2853891438144
cafe.append('banapresso')
print(cafe, id(cafe)) # ['starbucks', 'tomntoms', 'hollys', 'banapresso'] 2853891438144

cafe.insert(2,'start')
print(cafe) #['starbucks', 'tomntoms', 'start', 'hollys', 'banapresso']
cafe.insert(100000,'end')
print(cafe) #['starbucks', 'tomntoms', 'start', 'hollys', 'banapresso', 'end']

cafe.extend(['cup'])
print(cafe)
#['starbucks', 'tomntoms', 'start', 'hollys', 'banapresso', 'end', 'cup']

num = [1, 2, 3, 'hi']
print(num)
num.remove('hi')
print(num) #[1, 2, 3]
# num.remove('hii') -> 없는거 지우려고 하면 에러가 난다!

nums = [1, 2, 3, 'hi'] 
print(nums) # [1, 2, 3, 'hi']
word = nums.pop()
print(word) # hi
print(nums) # [1, 2, 3]

num = [1, 2, 3, 1, 1, 1, 2]
print(num.count(1)) # 4
print(num.count(100)) # 0

# num.sort() 와 sorted(num)의 차이가 있다!!!!!! 꼭 알아두기!!
num2 = [3, 2, 5, 7]
result = num2.sort()
print(num2, result) # [2, 3, 5, 7] None

num2 = [3, 2, 5, 8]
result = sorted(num2)
print(num2, result) # [3, 2, 5, 8] [2, 3, 5, 8]



day_name = ('월', '화', '수', '목', '금')

print(day_name[-3]) # 수
print(day_name * 2)
print(id(day_name)) # 2586933677488
day_name += False, True
print(day_name)
print(id(day_name)) # 2586934249024

print('apple' in 'a') # False
print('a' in 'apple') # True
print('서순' in ['서순', '무엇일까요', '기러기']) # True


a = {'사과', '바나나', '수박'}
a.add('딸기')
print(a) # {'사과', '딸기', '수박', '바나나'}, '딸기'의 위치가 바뀐다!

a.update(['딸기', '바나나', '참외'])
print(a) # {'바나나', '참외', '수박', '사과', '딸기'}

a.remove('사과')
print(a) # {'수박', '참외', '바나나', '딸기'}
#a.remove('사과')
#print(a) -> KeyError: '사과' 삭제할 것이 없을 땐 에러가 난다!

a.discard('사과')
print(a) # {'바나나', '딸기', '수박', '참외'} -> 없으면 없는대로!


my_dict = {'apple':'사과', 'banana':'바나나'}
data = my_dict.pop('apple')
print(data, my_dict) # 사과 {'banana': '바나나'}
data = my_dict.pop('apple',3)
print(data) # pop할 값이 없으면 '3'을 출력

my_dict = {'apple':'사', 'banana':'바나나'}
my_dict.update(apple='사과') # apple은 key 값!!
print(my_dict)


my_dict = {'apple':'사과', 'banana':'바나나'}

for key in my_dict:
    print(key)
# apple
# banana

for value in my_dict.values():
    print(value)
# 사과
# 바나나

for key,value in my_dict.items():
    print(f'{key} / {value}')
# apple / 사과
# banana / 바나나


'''
얕은 복사와 깊은 복사(shallow copy & deep copy)
'''

original_list = [1, 2, 3]
copy_list = original_list
print(original_list, copy_list) # [1, 2, 3] [1, 2, 3]

copy_list[0] = 'hello'
print(original_list, copy_list) # ['hello', 2, 3] ['hello', 2, 3]

a = [4, 5, 6]
b = a[:]
print(a, b) # [4, 5, 6] [4, 5, 6]

b[0] = 'bye'
print(a, b) # [4, 5, 6] ['bye', 5, 6]

# deep copy 하는 법은 모듈로 불러온다!
import copy
a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
b = copy.deepcopy(a)
print(a, b) 
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]] [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
b[0][2] = 'hello'
print(a, b)
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]] [[1, 2, 'hello'], [4, 5, 6], [7, 8, 9]]  