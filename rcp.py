import random
random_number = random.randint(1, 3)

hand_list=list('묵찌빠')

victory = 0
defeat = 0
draw = 0

com_hand=''
if random_number==1:
    com_hand="묵"
elif random_number==2:
    com_hand='찌'
else:
    com_hand='빠'

user_hand=input('묵, 찌, 빠 중 하나를 선택하세요: ')
while True:
    if user_hand not in hand_list:
        print('유효한 입력이 아닙니다')
        user_hand = input('묵, 찌, 빠 중 하나를 선택하세요: ')
    else:
        if user_hand == com_hand:
            print(f'사용자: {user_hand}, 컴퓨터: {com_hand}')
            print('비겼습니다')
            draw += 1
        elif (user_hand=='묵' and com_hand=='찌') or (user_hand=='찌' and com_hand=='빠') or (user_hand=='빠' and com_hand=='묵'):
            print(f'사용자: {user_hand}, 컴퓨터: {com_hand}')
            print('이겼습니다!')
            victory += 1
        else:
            print(f'사용자: {user_hand}, 컴퓨터: {com_hand}')
            print('졌습니다!')
            defeat += 1

        retry=input('다시 하시겠습니까? (y/n): ')
        if retry=='y':
            user_hand = input('묵, 찌, 빠 중 하나를 선택하세요: ')
        elif retry=='n':
            print('게임을 종료합니다')
            print(f'승: {victory}, 패: {defeat}, 무승부: {draw}')
            break
        else:
            while True:
                if retry=='y':
                    break
                elif retry=='n':
                    break
                else:
                    retry=input('다시 입력하세요. 다시 하시겠습니까? (y/n): ')
