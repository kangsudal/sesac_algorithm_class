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