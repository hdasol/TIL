#1 Mutable & Immutable
mutable = ['String', 'List', 'Set', 'Dictionary']
immutable = ['Tuple', 'Range']

#2 Dictionary 만들기
dict_stu = {'조원희':'26', '정민우':'26', '황다솔':'29', '강정훈':'26'} 

#3 평균 구하기
scores = [80, 89, 99, 83]
avg = (scores[0]+scores[1]+scores[2]+scores[3])/4
print(avg)

'''
Daily Workshop
pyton 02. 데이터 타입 밓 형 변환
'''
#1 숫자의 입력과 출력
num1 = int(input('첫 번째 수 입력: '))
num2 = int(input('두 번째 수 입력: '))
print(num1 + num2)

#2 dictionary를 활용하여 평균 구하기
menu = {'김밥':3000, '아라비아따':12000, '김치찌개':9000, '돼지국밥':8500}
price = list(map(int, menu.values()))
menu_avg = float(sum(price)/4)
print(menu_avg)
