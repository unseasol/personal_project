import random
world_record=99
answer=int(input("숫자를 입력하세요: "))
high_score=0
while True:
    random_number = random.randint(1, 100)
    if answer > 100:
        print('유효한 범위 내의 숫자를 입력하세요')
        answer=int(input('숫자를 입력하세요: '))
    elif answer < 1:
        print('유효한 범위 내의 숫자를 입력하세요')
        answer = int(input('숫자를 입력하세요: '))
    else:
        # print(random_number)
        high_record = 0
        while True:
            if answer < random_number:
                print('up')
                high_record += 1
                answer = int(input("숫자를 입력하세요: "))
            elif answer > random_number:
                print('down')
                high_record += 1
                answer = int(input("숫자를 입력하세요: "))
            else:
                high_record += 1
                break
            high_score=high_record
        if high_score < 4:
            print(f'wow! {high_score}번만에 맞췄습니다! 개고수')
        else:
            print(f'{high_score}번 시도해서 맞았습니다')
        if world_record>high_score:
            world_record=high_score
        retry=input('다시 하시겠습니까? (y/n): ')
        if retry=='y':
            print(f'이전 게임 플레이어 최고 시도 횟수: {world_record}')
            answer=int(input('숫자를 입력하세요: '))
        elif retry=='n':
            print(f'이번 게임의 최고 횟수: {world_record}')
            print('게임을 종료합니다')
            break
        else:
            while True:
                if retry=="y":
                    break
                elif retry=='n':
                    break
                else:
                    retry=input("문자를 다시 입력해주세요: ")
            print(f'이전 게임 플레이어 최고 시도 횟수: {high_record}')
            answer = int(input('숫자를 입력하세요: '))