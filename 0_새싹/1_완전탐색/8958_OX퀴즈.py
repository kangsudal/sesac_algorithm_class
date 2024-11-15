import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    results = input().rstrip()

    # 누적값, 최종점수값 세팅
    acc = score = 0

    # 반복문을 통해 results를 순회하며
    for result in results:
        # O가 나왔다면?
        if result == 'O':
            # 누적값 += 1
            acc += 1
            # 최종점수 += 누적값
            score += acc

        # X가 나왔다면?
        elif result == 'X':
            # 누적값을 초기화
            acc = 0

    # 최종점수를 출력
    print(score)