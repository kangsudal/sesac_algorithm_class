import sys
sys.setrecursionlimit(10**9)

def fibo(N):
    # 종료조건(N < 2)
    if N < 2:
        return N

    # fibo(N) = fibo(N-1) + fibo(N-2)
    return fibo(N-1) + fibo(N-2)

n = int(input())

print(fibo(n))

# 메모이제이션 기법
n = int(input())

memo = [0, 1]

for i in range(n-1):
    memo.append(memo[-1]+memo[-2])

print(memo[n])