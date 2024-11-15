# 한 줄에 하나씩 주어지는 숫자 N개 리스트로 받기
"""
nums = [int(input()) for _ in range(N)]
# 리스트 컴프리헨션(list comprehension)
"""
# 백준 문제의 경우 readline 통해 입력받기
"""
import sys
input = sys.stdin.readline
# readline 통해 입력받으면 끝에 개행문자 붙으므로
# 그냥 사용하려면 input().rstrip()으로 떼고 사용
"""
