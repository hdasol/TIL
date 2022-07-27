# 1452.데일리과제6-2.데이터 구조 복습 및 심화 예제1

'''
n개의 소금물을 섞었을 때, 혼합된 소금물의 농도와 양을 계산하는 프로그램
mass_percent.py를 만드시오.

조건
- 소금물의 퍼센트 농도와 소금물의 양을 입력하고, Done을 입력하면 혼합물의
퍼센트 농도와 양이 출력되도록 하시오. 최대 5개의 소금물을 입력할 수 있다.
출력된 혼합물의 퍼센트 농도와 양이 소수점 2자리를 넘어갈 경우, 반올림하여
2번째 자리까지만 나타내시오.

소금물의 농도 = 소금의 양 / 소금물의 양 *100
소금의 양 = 소금물의 농도 / 100 * 소금물의 양

'''

n = 1
salt, salt_water = [], []


while True:

    a = input('소금물의 농도(%)와 소금물의 양(g)을 입력하시오: ')

    #print(a) # 1% 400g
    #print(a.split()) #['1%', '400g']
   
    if a == 'Done':
        break
    else:
        a1 = a.replace('g', '').replace('%', '').split() # ['1', '400']

        salt_water.append(int(a1[1]))
        salt.append(float(int(a1[0])/100)*int(a1[1]))

        
print(f'{(sum(salt)/sum(salt_water))*100}% {sum(salt_water)}g')







