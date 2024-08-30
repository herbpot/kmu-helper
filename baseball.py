import random as rn
import sys


def check(arr):
    if len(arr) != 3 or len(set(arr)) < 3:
        return True
    else:
        return False


answer = []
while True:
    if not answer:
        answer = [rn.randrange(1, 10), rn.randrange(1, 10), rn.randrange(1, 10)]
        while check(answer):
            answer = [rn.randrange(1, 10), rn.randrange(1, 10), rn.randrange(1, 10)]

    print("숫자 야구 게임을 시작합니다.")
    # print(answer)

    user = list(map(int, input()))
    cnt = 0
    while True:
        if not check(user):
            break
        cnt += 1
        print("잘못된 입력입니다. 연속 실패:", cnt)

        if cnt == 3:
            print("error")
            sys.exit()

        user = list(map(int, input()))

    s_cnt = 0
    b_cnt = 0
    for i in range(0, 3):
        for j in range(0, 3):
            if user[i] == answer[j]:
                if i == j:
                    s_cnt += 1
                elif i != j:
                    b_cnt += 1
                break
    if s_cnt == 0 and b_cnt == 0:
        print("OUT")
    elif s_cnt == 3:
        answer = []
        print("3S")
        print("3개의 숫자를 모두 맞히셨습니다.")
        if input("게임을 새로 시작하려면 Y, 종료하려면 N를 입력하세요.") == 'N':
            break

    elif s_cnt == 0:
        print(f"{b_cnt}B")
    elif b_cnt == 0:
        print(f"{s_cnt}S")
    else:
        print(f"{b_cnt}B {s_cnt}S")
