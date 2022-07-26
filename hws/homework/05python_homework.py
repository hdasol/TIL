'''
데일리 홈워크 python 05. 데이터 구조 및 활용
'''

# 01. 모음은 몇 개나 있을까?

word = 'banana'
aeiou = ['a', 'e', 'i', 'o', 'u']

def count_vowels(word):
    count = 0
    for i in word:
        if i in aeiou:
            count = count + 1
    return count
print(count_vowels(word))

# 02. 문자열 조작
# 정답 4번 -> 특정 문자를 지정하지 않으면 오류가 아니라 공백 제거!

# 03. 정사각형만 만들기

a = [32, 55, 63]
b = [13, 32, 40, 55]

def only_square_area(a, b):
    c = [] #넓이를 저장할 공간!
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                c.append(a[i]*b[j])
    return c

print(only_square_area(a, b))

'''
데일리 워크샵 python 06. 데이터 구조와 복사
'''

# 01. 평균 점수 구하기

scores = {'python':80, 'web':83, 'algorithm':90, 'django':89}
print(scores.values()) # dict_values([80, 83, 90, 89])

def get_dict_avg(scores):

    return sum(scores.values())/len(scores)

print(get_dict_avg(scores))

# 02. 혈액형 분류하기

blood_type = [
    'A', 'B', 'A', 'O', 'AB', 'AB',
    'O', 'A', 'B', 'O', 'B', 'AB']

def count_blood(blood_type):
    count_A = 0
    count_B = 0
    count_AB = 0
    count_O = 0

    for i in range(len(blood_type)):
        if blood_type[i] == 'A':
            count_A += 1
        elif blood_type[i] == 'B':
            count_B += 1
        elif blood_type[i] == 'AB':
            count_AB += 1
        else:
            count_O += 1
    return {'A':count_A, 'B':count_B, 'O':count_O, 'AB':count_AB,}

print(count_blood(blood_type))


