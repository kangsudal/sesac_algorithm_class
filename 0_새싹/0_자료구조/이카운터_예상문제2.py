from collections import Counter
N=int(input())
v_list = list(map(int,input().split()))
count_v_list = Counter(v_list)

result = []
for num in set(v_list):
    if count_v_list[num]==1:
        result.append(num)

print(len(result))