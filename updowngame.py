import random

best = 10 # 최고 기록을 10으로 초기값을 둬서 첫번째 도전한 사람의 점수가 최고 점수가 되도록 함
score = [] # 기록 저장하는 리스트

while True:
    answer = random.randrange(1, 101)  # 1부터 100까지의 난수 값 생성
    print("UP & DOWN 게임에 오신걸 환영합니다~")
    print("1. 게임시작 2. 기록확인 3. 게임종료")
    menu = input(">>")

    if menu == '1':
        start = 1
        end = 100
        for i in range(1, 11):
            number = int(input("%d번째 숫자 입력(%d~%d) : " %(i,start,end)))
            if number == answer:
                print("정답입니다!!\n%d번째만에 맞추셨습니다" %i)
                score.append(i)
                if i < best: # 정답을 맞췄을 때 시도 횟수가 best보다 작을 경우 best를 i로 초기화
                    print("최고기록 갱신~!")
                    best = i
                break
            else:
                if number > answer:
                    end = number
                    print("DOWN")
                else:
                    start = number
                    print("UP")

    elif menu == '2':
        record = set(score)  # 중복 제거
        list(record).sort() # 오름차순 정리
        index = 1
        for i in record:
            print("%d %d" %(index, i))
            index = index + 1

    else: # 1과 2를 제외한 값이 입력되면 종료
        break
