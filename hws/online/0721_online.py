'''
정수 0부터 9까지로 이루어진 list를 전달 받아, 연속적으로 나타나는 숫자는 하나만
남기고 제거한 list를 출력하라. 이때, 제거되고 남은 수들이 담긴 list의 요소들은
기존의 순서를 유지해야한다.

- 입력 예시
[1,1,3,3,0,1,1]
- 출력 예시
[1,3,0,1]
앞 수와 뒷 수가 같으면 뒷수 지움.
만약에 다르면 뒷 수 입력
'''

num = [1,1,3,3,0,1,1]


def solution(num):
    result = []
    result.append(num[0])

    for i in range(1, len(num)):
        if num[i-1] != num[i]:
            result.append(num[i])
    return result

print(solution(num))



    
    
        
     
    


    


