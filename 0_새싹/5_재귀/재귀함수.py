nums = []

#재귀함수를 이용해서 nums에서 가장 큰 수를 찾아보자
ans = 0

def find(depth):
    global ans
    #종료 조건
    #깊이가 10이라면 리턴
    if depth == 10:
        return

    #갱신 로직
    #정답 후보와 nums[dept]를 비교해서 큰 수로 갱신
    ans = max(ans, nums[depth])

    #다음 뎁스로 이동
    find(depth+1)

find(0)
print(ans)


def find(depth,ans):
    # 종료 조건
    # 깊이가 10이라면 리턴
    if depth == 10:
        return

    # 갱신 로직
    # 정답 후보와 nums[dept]를 비교해서 큰 수로 갱신
    ans = max(ans, nums[depth])

    # 다음 뎁스로 이동
    find(depth + 1)

find(0)
print(ans)