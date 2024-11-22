nums = [3, 5, 1, 4, 2]

# 방법1
acc = [0]
for num in nums:
    acc.append(acc[-1] + num)

print(acc)

# 방법2
from itertools import accumulate
acc2 = [0] + list(accumulate(nums))

print(acc2)