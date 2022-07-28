import random

is_playing = True

while is_playing:
    print('================================')
    print('        Up and Down Game        ')
    print('================================')

    answer = random.randint(1, 10000)  # 1이상 10000이하의 난수
    counts = 0  # 몇 번만에 정답을 맞혔는지 담는 변수

    # 여기부터 코드를 작성하세요.
    # 1. 숫자 입력 받기
    while True:
        print()

        # 1-1. 입력 문구
        num = int(input('1이상 10000이하의 숫자를 입력하세요: '))

        if num < 1 or num > 10000:
            print('잘못된 범위의 숫자를 입력하셨습니다. 다시 입력해주세요')
            continue
        
        counts += 1

        if num < answer:
            print('up!!')
        elif num > answer:
            print('down!!')
        else:
            print(f'{counts}회 만에 정답을 맞혔습니다')
            print()
            break

    user_choice = input('게임 재시작: y, 게임 종료: n')

    if user_choice == 'y':
        print()
        continue

    if user_choice == 'n':
        print('이용해주셔서 감사합니다. 게임을 종료합니다.')
    else:
        print('잘못된 값을 입력하셨습니다. 게임을 종료합니다.')
    
    is_playing = False