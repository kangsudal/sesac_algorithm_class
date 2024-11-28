# 현재 가지고있는 카드는 3이야.  다른카드는3,4,-1,-5가 있어.
# 이중에 한장 또는 여러장 카드를 뽑아 내 카드랑 합이 5가되려고하는 경우의 수가 뭐가있어?

from itertools import combinations
N, S, K = map(int, input().split())
card_list = list(map(int,input().split()))

need_value = S-K

count =0
for r in range(1,len(card_list)+1):
    #카드 1장부터 총 개수까지의 조합
    for subset in combinations(card_list,r):
        if sum(subset) == need_value:
            count += 1
            # print(f"가능한조합:{subset}")
print(count)