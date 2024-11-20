import sys
input = sys.stdin.readline

def is_palindrome(keyword):
    return keyword == keyword[::-1]

def find_pal():
    keywords = []
    # 몇개 단어?
    k = int(input().strip())

    for _ in range(k):
        keywords.append(input().strip())
    # 모든 경우의 문자열 구하기
    for i in range(k - 1):
        for j in range(i + 1, k):
            new_keyword = keywords[i] + keywords[j]
            if is_palindrome(new_keyword):
                print(new_keyword)
                return
            new_keyword2 = keywords[j] + keywords[i]
            if is_palindrome(new_keyword2):
                print(new_keyword2)
                return
    print(0)

T = int(input().strip())


for _ in range(T):
    find_pal()

#########
#강사님 풀이
import sys

input = sys.stdin.readline

# permutations 모듈 활용한 풀이
from itertools import permutations

T = int(input())
for _ in range(T):
    k = int(input())
    words = [input().rstrip() for _ in range(k)]
    # list comprehension, 지능형 리스트, 리스트 내포
    my_lst = [2 * i for i in range(10) if i % 2 == 0]
    print(words)

    for w1, w2 in permutations(words, 2):
        p = w1 + w2
        if p == p[::-1]:  # 회문 검사
            print(p)
            break

    else:
        print(0)

############################
# 1. flag 변수 활용
T = int(input())
for _ in range(T):
    k = int(input())
    words = [input().rstrip() for _ in range(k)]

    flag = False
    for i in range(k):
        for j in range(k):
            if i == j:
                continue

            p = words[i] + words[j]
            if p == p[::-1]:
                print(p)
                flag = True
                break
        if flag:
            break

    if not flag:
        print(0)

#################################
# 2. exit(0) 사용하기
T = int(input())
for _ in range(T):
    k = int(input())
    words = [input().rstrip() for _ in range(k)]

    for i in range(k):
        for j in range(k):
            if i == j:
                continue

            p = words[i] + words[j]
            if p == p[::-1]:
                print(p)
                exit(0)

    print(0)


####################################
# 3. 함수 처리하기
def find_palindrome():
    for i in range(k):
        for j in range(k):
            if i == j:
                continue

            p = words[i] + words[j]
            if p == p[::-1]:
                print(p)
                return

    print(0)


T = int(input())
for _ in range(T):
    k = int(input())
    words = [input().rstrip() for _ in range(k)]

    find_palindrome()