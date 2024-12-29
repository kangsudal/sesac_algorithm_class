import sys
input = sys.stdin.readline


T=int(input().rstrip())
for _ in range(T):
    H, W, N = map(int, input().rstrip().split())
    X = N//H+1
    Y = N%H
    print(str(Y)+f"{X:02d}")