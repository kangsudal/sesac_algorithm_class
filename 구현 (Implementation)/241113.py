import sys
input = sys.stdin.readline

#오타맨 고창영
# T = int(input())
#방법1
# for test_case in range(T):
#     idx, word = input().split()
#     idx = int(idx)-1
#
#     print(word[:idx]+word[idx+1:])

#방법2
# for _ in range(T):
#     idx, word = input().split()
#     idx = int(idx)-1
#     word = list(word)
#     word.pop(idx)
#
#     print(''.join(word))


#OX 퀴즈
# test_case = int(input())
# for _ in range(test_case):
#     results = input().rstrip()
#     # 누적값, 최종 점수 값 세팅
#     acc = score = 0
#     # 반복문을 통해 results를 순회하며
#     for result in results:
#         #O가 나왔다면?
#         if result == 'O':
#             #누적값 += 1
#             acc += 1
#             # 최종점수 += 누적값
#             score += acc
#         #X가나왔다면?
#         elif result == 'X':
#             #누적값을 초기화
#             acc = 0
#     #최종 점수를 출력
#     print(score)

# 백준 1920번 수 찾기(해시 자료구조)
N = int(input())
A = set(map(int, input().split()))

M = int(input())
B = list(map(int, input().split()))

# B를 순회하면서
for num in B:
    #A에 있다면? 1 출력
    if num in A:
        print(1)
    #없다면? 0 출력
    else:
        print(0)