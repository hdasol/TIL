# problem 01 전체 점수 중 최고점을 반환하는 함수 max_score을 완성하시오
'''
def max_score(scores):

    maximum = 0

    for i in scores:
        if i > maximum:
            maximum = i
    return maximum


def max_score(scores):
    return (max(scores))


def max_score(scores):
    scores.sort()
    return (scores[len(scores)-1])
'''

from itertools import count


scores = {'python':80, 'html':70, 'javascript':65, 'project':58}

print(scores.values()) # dict_values([80, 70, 65, 58])
print(scores['python']) # 80

a = [scores['python'], scores['html'], scores['javascript'], scores['project']]

print(a) #[80, 70, 65, 58]

def max_scores(a):

    maximum = 0

    for i in a:
        if i > maximum:
            maximum = i
    return maximum

print(max_scores(a)) #80

def over(a):

    count = 0 # 60점이 넘는 과목을 할당할 공간

    for j in a:
        if j >= 60:
            count += 1 #60점이 이상일 때 count 1씩 증가
    return count

print(over(a))

'''
def menu_count(a):
    return len(a['menus'])
'''

day_temp = {'0':38, '1':27}

b = [day_temp['0'], day_temp['1']]
print(b, type(b))  #[38, 27]
c = map(int,b)
print(c, type(c))

def turn(day_temp):
    sol = dict(maximum = [], minimum = [])

    b.sort() # b를 오름차순으로 정렬

    sol['maximum'].append(b[len(b)-1])
    sol['minimum'].append(b[0])

    return sol

print(turn(day_temp))


id = input('id 입력: ')
pw = input('pw 입력: ')

user_data = {'user_id':id, 'user_pw':pw}

def is_user_data_vaild(user_data):

    if user_data['user_id'] == '' or user_data['user_pw'] == '':
        return False
    else:
        return True

print(is_user_data_vaild(user_data))

def is_id_vaild(user_data):

    x = user_data['user_id']
   
    if x[len(x)-1] in map(str, range(10)):
        return True
    else:
        return False

print(is_id_vaild(user_data))
