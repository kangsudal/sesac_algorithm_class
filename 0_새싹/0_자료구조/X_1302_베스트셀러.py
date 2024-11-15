# dict로 푸는 문제
import sys
input = sys.stdin.readline

N = int(input())
book_sales = dict()

for _ in range(N):
    book_name=input().rstrip()

    #키값이 존재하는경우
        # +=1

    #키값이 존재하지 않는 경우
        #새로 생성(book_name : 1)

#가장 많이 팔린 책 찾기
#선형탐색
#초기값 설정
max_sales = 0
max_sales_book_name = ''

# 딕셔너리를 선형탐색하면서
    #만약 그 책이 max_sales보다 많이 팔렸다면
        #max_sales_book 갱신
    #만약 똑같이 팔렸다면?
        #더 작은 책 제목으로 갱신