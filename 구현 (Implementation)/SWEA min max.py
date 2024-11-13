def find_min_max(nums_param):
    smallest = float("INF")
    biggest = -float("INF")
    for num in nums_param:
        if num<smallest:
            smallest = num
        if num>biggest:
            biggest = num
    return {'smallest':smallest,'biggest':biggest}


T = int(input())
for test_case in range(1,T+1):
    N=int(input())
    nums = list(map(int,input().split(' ')))
    result = find_min_max(nums)
    print(f"#{test_case} {abs(result['biggest']-result['smallest'])}")