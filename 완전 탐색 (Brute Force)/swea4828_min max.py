import sys
input = sys.stdin.readline

T=int(input().rstrip())

for t in range(T):
    N=int(input().rstrip())
    a = list(map(int,input().rstrip().split()))
    print(f'#{t+1} {abs(max(a)-min(a))}')