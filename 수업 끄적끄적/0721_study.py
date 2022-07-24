houses = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for house in houses:
    if house == 1:
        print('전력을 차단하지 말아주세요')
        break
else:  # 여기서 else 는 위에서 단 한번이라도 break 가 걸리지 않을 경우만 발동합니다.
    print('작업을 시작해도 될 것 같아요')

nums = [1, 5 ,77, 26, 33, 2, 6, 16, 55]

print(max(nums))
print(min(nums))

max_num = -1 # 될 수 없을만큼 '작은' 숫자로 초기화 한다!!!!!

for num in nums:
    if max_num < num:
        max_num = num
print(max_num)

matrix = [[1, 8, 4], [7, 3, 9], [5, 2, 6]]
r = 1
c = 1
print(matrix[r][c])

# 행우선순회??????
for r in range(3):
    for c in range(3):
        print(matrix[r][c], end=' ')

print()

for r in range(3):
    for c in range(3):
        print(matrix[c][r], end=' ')
print()

for r in range(3):
    for c in range(3):
        print(matrix[r][c], end=' ')
    print()

# 스트링을 만들 수 있는 메소드를 사용할 줄 알아야한다!
nums = input('수 입력: ')
print(nums, type(nums))
nums_list = nums.split()
print(nums_list, type(nums_list[0]))

cover = 0

for cover, i in enumerate(nums_list):
    nums_list[cover] == int(i)
    cover = cover + 1

print(nums_list, type(nums_list[0]))

map_object = map(int, nums_list)
list_flavour = list(map_object)
print(list_flavour, type(list_flavour[0]))

nums = list(map(int, input('수 입력: ').split()))
print(nums, type(nums[0]))

a = list(input('띄어쓰기 없이 수 입력: '))
print(a)