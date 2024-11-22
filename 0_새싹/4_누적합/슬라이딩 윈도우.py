import sys
input = sys.stdin.readline

N, K = map(int, input().split())
nums = list(map(int, input().split()))

# 일단 첫번째 구간의 합은 구해놓는다
ans = tmp = sum(nums[:K])

# N-K+1번 반복
for i in range(N-K):
    # tmp = sum(nums[i:i+K])
    tmp += nums[i+K] - nums[i]
    # 정답을 갱신
    ans = max(ans, tmp)

print(ans)

'''
3. 구간합 문제
    1. 1차원 배열의 일정한 구간의 합을 구하는 문제
    2. 나이브한 풀이
        1. 반복문을 돌며 해당하는 구간의 합을 그때그때 새롭게 구하기
    3. 슬라이딩 윈도우
        1. N+1번째 구간합은 N번째 구간합과 대부분의 구간을 공유 ⇒ 새로 구하는 것은 비효율적
        2. 앞뒤로 두 번의 연산만 해주면 새로운 구간합을 구할 수 있음
        3. 구간의 길이가 고정되어 있는 문제
    4. 누적합 알고리즘
        1. 구간의 길이가 변한다면, 모든 구간의 합에 대한 정보를 **미리** 계산해두자!
        2. accumulate 모듈 이용한 누적합 배열 제작(앞에 0 붙이면 인덱스 계산 편함)'''