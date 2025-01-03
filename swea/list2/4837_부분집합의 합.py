import itertools

def untill_num_array(num):
    arr=[]
    for n in range(1,num+1):
        arr.append(n)
    return arr

def combination_arr(arr,r):
    nCr = []
    nCr.extend(list(itertools.combinations(arr, r)))
    return nCr

T = int(input())
A = untill_num_array(12)

for test_case in range(1,T+1):
    count = 0
    N, K = map(int, input().split())
    r= N
    for arr in combination_arr(A,r):
        if sum(arr) == K:
            count += 1
    print(f'#{test_case} {count}')
