N = int(input())
A = set(map(int, input().split()))

M = int(input())
B = list(map(int, input().split()))

# B를 순회하면서
for num in B:
    # A에 있다면? 1 출력
    if num in A:
        print(1)
    # 없다면? 0 출력
    else:
        print(0)