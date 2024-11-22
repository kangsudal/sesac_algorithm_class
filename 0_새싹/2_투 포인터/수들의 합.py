import sys

input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))
cnt = 0
# 포인터 초기화(세팅)
l, r = 0, 0
tmp = 0

while True:
    # tmp < M
    if tmp < M:
        # r값이 끝에 도달했다면?
        if r == N:
            # 종료
            break
        # 오른쪽 포인터가 가리키는 값을 tmp에 더하고
        tmp += nums[r]
        # 오른쪽 포인터 이동
        r += 1

    # tmp > M
    elif tmp > M:
        # 왼쪽 포인터가 가리키는 값을 tmp에서 빼고
        tmp -= nums[l]
        # 왼쪽 포인터 이동
        l += 1

    # tmp == M
    elif tmp == M:
        # cnt += 1
        cnt += 1
        # 왼쪽 포인터가 가리키는 값을 tmp에서 빼고
        tmp -= nums[l]
        # 왼쪽 포인터 이동
        l += 1

print(cnt)