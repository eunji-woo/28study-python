import random

record = [] # 기록 저장하는 리스트

while True:
    answer = random.randrange(1, 101)  # 1부터 100까지의 난수 값 생성
    print("UP & DOWN 게임에 오신걸 환영합니다~")
    print("1. 게임시작 2. 기록확인 3. 게임종료")
    menu = input(">>")

    if menu == '1':
        start = 1
        end = 100
        for i in range(1, 11):
            while True: # 피드백 1번 (정답으로 1~100 범위 안에 해당하지 않는 숫자는 입력 불가능하게 하기)
                number = int(input("%d번째 숫자 입력(%d~%d) : " % (i, start, end)))
                if number <= 100 and number >= 1: break
                else: print("1부터 100까지의 수를 입력해주세요.")

            if number == answer:
                print("정답입니다!!\n%d번째만에 맞추셨습니다" %i)
                if len(record) == 0: # 맨 처음 실행의 경우 무조건 최고 기록으로 저장
                    print("최고기록 갱신~!")
                    record.append(i) # best 리스트 맨 뒤에 최고기록 저장
                    # 피드백 3번 (최고기록만 기록에 추가해주기)
                    nickname = int(input("최고기록 갱신~! \n닉네임을 입력해주세요: "))

                elif i < record[-1]: # best 리스트 맨 뒤에 저장되어있는 최고기록과 현재 기록을 비교
                    print("최고기록 갱신~!")
                    record.append(i)  # best 리스트 맨 뒤에 최고기록 저장
                break  # 정답인 경우 종료
            else:
                if number > answer:
                    print("DOWN")
                    if number < end: # 피드백 2번 (답 입력 후 범위가 축소된 경우 해당 범위에 속하지 않는 답을 입력하면 범위가 다시 늘어나지 않게 하기)
                        end = number

                elif number < answer:
                    print("UP")
                    if number > start: # 피드백 2번 (답 입력 후 범위가 축소된 경우 해당 범위에 속하지 않는 답을 입력하면 범위가 다시 늘어나지 않게 하기)
                        start = number

    elif menu == '2':
        index = 1
        for i in reversed(record):
            print("%d %d" %(index, i))
            index = index + 1

    elif menu == '3':
        break

    else: # 1과 2, 3를 제외한 값이 입력되면 종료
        print("다시 입력해주세요")
