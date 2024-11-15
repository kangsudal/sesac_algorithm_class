#2중포문을 쓰면 O(N^2)
# dwarfs = [int(input()) for _ in range(9)]
# dwarfs.sort()
# spy=[]
# flag = False
# for i in range(8):
#     for j in range(i+1,9):
#         if sum(dwarfs) - dwarfs[i] - dwarfs[j] == 100:
#             spy = [i,j]
#             flag = True
#             break
#         if flag:
#             break
#
# for idx in range(9):
#     if idx in spy:
#         continue
#     print(dwarfs[idx])

#########################################################
#9C2 : 9개 데이터 셋에서 2개를 뽑는 경우의 수 : 조합 문제
from itertools import combinations

dwarfs = [int(input()) for _ in range(9)]
dwarfs.sort()
# spy=[]

for spy1, spy2 in combinations(dwarfs,2):
    if sum(dwarfs) - spy1 - spy2 ==100:
        spy = [spy1, spy2]
        break
for dwarf in dwarfs:
    if dwarf not in spy:
        print(dwarf)