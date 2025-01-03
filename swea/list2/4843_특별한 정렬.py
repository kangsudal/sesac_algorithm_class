def selection_sort(a):
    for i in range(0,len(a)-1):
        min = i
        for j in range(i+1,len(a)):
            if i % 2 == 0:
                if a[min] < a[j]:
                    min = j
            else:
                if a[min] > a[j]:
                    min = j
        a[i],a[min] = a[min],a[i]

T=int(input())
for test_case in range(1,T+1):
    N=int(input())
    a = list(map(int,input().split()))
    selection_sort(a)
    print(f'#{test_case}',end=' ')
    for i in range(10):
        if i == 9:
            print(a[i])
        else:
            print(a[i],end=' ')