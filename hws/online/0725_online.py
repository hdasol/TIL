'''
어떤 해가 입력되면 그 해가 윤년인지 아닌지 판별하는 함수를 만드시오.
윤년 판단조건
-해가 4의 배수면서 100배수가 아니면 유년
-400의 배수이면 유년
-위의 두 조건 중 하나라도 맞으면 윤년이다.

'''

def leap_year(year):

    if year%4==0 and year%100!=0:
        return (str(year)+'년은 윤년입니다')
    elif year%400==0:
        return (str(year)+'년은 윤년입니다')
    else:
        return (str(year)+'년은 윤년이 아닙니다')

print(leap_year(2021))
print(leap_year(2020))