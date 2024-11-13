gems = [3, 3, 1, 2, 3, 2, 2, 3, 3, 1]

grade_lst = [0] * 4
for gem in gems:
    grade_lst[gem] += 1

print(grade_lst)

#3.nums 리스트에서 가장 큰 수, 가장 작은 수를 뽑는 로직

nums = [-1, 5, 23, 3, 123, 121, 120, 125, 56, -17]

the_minnest = -float('INF')# the_minnest = nums[0]
the_biggest = float('INF')# the_biggest = nums[0]
for num in nums:
    if num < the_minnest:
        the_minnest = num
    if num > the_biggest:
        the_biggest = num

print(the_minnest)
print(the_biggest)