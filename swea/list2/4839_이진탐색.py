T=int(input())

def binary_search(low, high, target):
    count = 0
    while low <= high:
        mid = (low+high) // 2
        count += 1
        if target == mid:
            return count
        elif target < mid:
            high = mid
        elif target > mid:
            low = mid
    # return -1

for test_case in range(1,T+1):
    P,P_a,P_b = map(int,input().split())
    print(f'#{test_case}',end=' ')
    count_a = binary_search(1,P,P_a)
    count_b = binary_search(1,P,P_b)
    if count_a < count_b:
        print('A')
    elif count_a > count_b:
        print('B')
    else:
        print("0")