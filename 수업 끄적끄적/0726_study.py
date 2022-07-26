a = [
    [3, 1, 2],
    [4, 7, 9],
    [6, 8, 5] 
]

print('original matrix: ', a) # [[3, 1, 2], [4, 7, 9], [6, 8, 5]]

#for r in range(3):
#    for c in range(3):
#        a[r][c], a[c][r] = a[c][r], a[r][c]
# 이 코드는 스왑하고 또 스왑하는 제자리 코드다! 전치의 전치!!
# 전치는 딱 3번 만 하면 돼!

for r in range(3):
    for c in range(3):
        if r > c:
            a[r][c], a[c][r] = a[c][r], a[r][c]

print('original matrix: ', a) # [[3, 4, 6], [1, 7, 8], [2, 9, 5]]
# 이 코드의 문제점???? 정방행렬에서만 잘 돌아갈 것이다!!! 3*4는?
# zip을 사용하면 할 수 있음!!!!

a = [
    [3, 1, 2],
    [4, 7, 9],
    [6, 8, 5] 
]

transposed_matrix = list(zip(*a))
print('original matrix: ', a) #[[3, 1, 2], [4, 7, 9], [6, 8, 5]]
print('transposed matrix: ', transposed_matrix) #[(3, 4, 6), (1, 7, 8), (2, 9, 5)]
# zip은 튜플로 반환한다!!! 

list_transposed_matrix = list(map(list, zip(*a)))
print('listtransposed matrix: ', list_transposed_matrix)
# listtransposed matrix:  [[3, 4, 6], [1, 7, 8], [2, 9, 5]]



nums = [1, 2, 3, 4, 5]

def a():
    nums = [9, 10, 11, 12, 13]
    print(nums[4])

print(a()) # 13 None -> return 값이 없어서 None이 출력
a() # 13
print(nums[4]) # 5
